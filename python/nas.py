import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/world/sise.nhn?symbol=NAS@IXIC'
response = requests.get(url).text # 요청 보내고 받은 응답 text 변환
data = BeautifulSoup(response, 'html.parser') #응답으로 받은거 처리하기 쉽게 가공(parsing)
nas = data.select_one('#content > div.rate_info > div.today > p.no_today')
result1 = nas.text

print(f'나스닥 지수는 {result1}입니다.')