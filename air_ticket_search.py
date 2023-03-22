import requests
from bs4 import BeautifulSoup

url = "https://www.koreanair.com/korea/ko/booking/flight-select"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

params = {
    "tripType": "OW",
    "origin": "GMP",
    "destination": "CJU",
    "flightDate": "20230404",
    "adultPaxCnt": "1",
    "childPaxCnt": "0",
    "infantPaxCnt": "0",
    "teenPaxCnt": "0",
    "cabinClass": "Y",
    "promotionCode": ""
}

response = requests.post(url, headers=headers, params=params)
soup = BeautifulSoup(response.content, "html.parser")
price = soup.select_one(".currency > .price > strong").get_text()

print(price)
