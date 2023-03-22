import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 각 골프장의 예약 가능 날짜를 크롤링할 URL
urls = {
    '크라운CC': 'https://www.crowncountryclub.co.kr/reserve/list.asp?intPageSize=500&intCurrPage=1',
    '세인트포CC': 'https://www.stpcc.co.kr/reserve/list.asp?intPageSize=500&intCurrPage=1',
    '스프링데일CC': 'https://www.sdcc.co.kr/reserve/list.asp?intPageSize=500&intCurrPage=1',
    '아난티CC': 'https://www.anantacountryclub.com/reserve/list.asp?intPageSize=500&intCurrPage=1',
    '중문CC': 'https://www.jungmuncc.co.kr/reserve/list.asp?intPageSize=500&intCurrPage=1',
}

# 크롤링할 예약 날짜 범위
start_date = datetime.today()
end_date = start_date + timedelta(days=7)

# 각 골프장의 예약 가능 날짜를 저장할 딕셔너리
available_dates = {}

# 각 골프장마다 크롤링 실행
for name, url in urls.items():
    try:
        # requests를 사용해 URL에 GET 요청을 보냄
        response = requests.get(url, verify=False)
        
        # BeautifulSoup을 사용해 HTML 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 예약 가능 날짜가 저장된 td 태그들을 찾음
        tds = soup.find_all('td', {'class': 'day'})

        # 예약 가능 날짜를 저장할 리스트
        dates = []

        # td 태그들을 순회하며 예약 가능 날짜를 리스트에 저장
        for td in tds:
            date_str = td.find('a').text.strip()
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if start_date <= date <= end_date:
                dates.append(date.strftime('%Y-%m-%d'))

        # 결과를 딕셔너리에 저장
        available_dates[name] = dates

    except requests.exceptions.SSLError:
        print(f'SSL Error occurred while connecting to {name}.')
        continue

    except requests.exceptions.ConnectionError:
        print(f'Connection Error occurred while connecting to {name}.')
        continue

# 결과 출력
for name, dates in available_dates.items():
    print(f'{name}: {dates}')