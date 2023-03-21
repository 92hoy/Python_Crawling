import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def download_images(query, num_images):
    # 검색어를 이용해 Google 이미지 검색 URL 생성
    url = 'https://www.google.com/search?q=' + quote(query) + '&tbm=isch'

    # HTTP 요청 보내고 응답 받기
    try:
        html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    except requests.exceptions.RequestException as e:
        print('Error occurred while sending request:', e)
        return

    # HTML 문서 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 이미지 링크 추출
    links = []
    for img in soup.find_all('img'):
        link = img.get('src')
        if link is not None and link.startswith('http'):
            links.append(link)

    # 이미지 다운로드
    save_dir = 'images'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    count = 0
    for link in links:
        if count == num_images:
            break

        try:
            response = requests.get(link, stream=True, headers={'User-Agent': 'Mozilla/5.0'})

            if response.status_code == 200:
                # 이미지 파일 저장
                filename = '{}_{}.jpg'.format(query, count)
                image_path = os.path.join(save_dir, filename)
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)

                print('{} saved.'.format(image_path))
                count += 1
            else:
                print('Failed to download image: {}'.format(link))

        except requests.exceptions.RequestException as e:
            print('Error occurred while downloading image:', e)

    print('{} images downloaded.'.format(count))


# 검색어와 저장할 이미지 개수 지정
query = 'paper'
num_images = 10

download_images(query, num_images)
