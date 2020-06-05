import urllib.request
from bs4 import BeautifulSoup
import requests

car_url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=2019+%ED%8E%A0%EB%A6%AC%EC%84%B8%EC%9D%B4%EB%93%9C'
resp = requests.get(car_url)
soup = BeautifulSoup(resp.content, 'html.parser')
car = soup.select('#main_pack > div.content_search.section > div > div.contents03_sub > div > div.profile_wrap > dl > dt.name > a > strong')
print(type(car))
print(car)
# 텍스타만 출력
print(car[0].text)
car_image = soup.select('#main_pack > div.content_search.section > div > div.contents03_sub > div > div.profile_wrap > div.thumb_profile > a > img')
print(car_image)

# 세부페이지로 가는링크
detail_link = soup.select('#main_pack > div.content_search.section > div > div.contents03_sub > div > div.profile_wrap > dl > dt.name > a')
print(detail_link)
print(detail_link[0].get('href'))
#차 세부 이미지
car_detail = 'https://auto.naver.com/car/main.nhn?yearsId=128143'
resp = requests.get(car_detail)
soup = BeautifulSoup(resp.content, 'html.parser')
detail = soup.select('#carMainImgArea > div.main_img > img')
print(detail[0].get('src'))