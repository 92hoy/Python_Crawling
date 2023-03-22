import requests
from bs4 import BeautifulSoup

"""
제품 가격 추적 및 비교 서비스
쇼핑몰은 위메프 와 티몬 두가지를 비교
"""

# 우선 원하는 제품의 URL을 가져와서 HTML 코드를 가져오기 ['아이폰 12 128GB']
wemakeprice_url = 'https://front.wemakeprice.com/product/919580943'
tmon_url = 'http://www.tmon.co.kr/deal/3515122936'

wemakeprice_response = requests.get(wemakeprice_url)
tmon_response = requests.get(tmon_url)

wemakeprice_html = wemakeprice_response.text
tmon_html = tmon_response.text

# HTML 코드를 BeautifulSoup 라이브러리를 사용하여 파싱
wemakeprice_soup = BeautifulSoup(wemakeprice_html, 'html.parser')
tmon_soup = BeautifulSoup(tmon_html, 'html.parser')

# 제품 정보를 추출 -> 제품 이름, 가격
wemakeprice_name = wemakeprice_soup.find('h3', {'class': 'tit'}).text.strip()
wemakeprice_price = wemakeprice_soup.find('strong', {'class': 'sale_price'}).text.strip()

tmon_name = tmon_soup.find('h1', {'class': 'tit'}).text.strip()
tmon_price = tmon_soup.find('span', {'class': 'value'}).text.strip()

# 추출한 제품 정보를 출력
print('위메프 제품명:', wemakeprice_name)
print('위메프 가격:', wemakeprice_price)
print('티몬 제품명:', tmon_name)
print('티몬 가격:', tmon_price)