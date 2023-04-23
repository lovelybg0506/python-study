import requests               # 크롤러의 기본 웹사이트접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 크롤러의 기본 HTML 분석해주는 라이브러리
import urllib.request         # 이미지관련 라이브러리

samsung = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

# print(samsung.content) # 웹페이지에 들어있는 모든 HTML 데이터
# print(samsung.status_code) # 그 웹페이지 접속 제대로 되고 있나 확인 가능 [200] / 400,500 = 오류

soup = BeautifulSoup(samsung.content, 'html.parser') # html코드를 정돈되게 바꿔줌

# print(soup.find_all("strong", id="_nowVal")[0].text) # 태그명과 속성으로 찾기 (찾은결과는 리스트[]로 뱉어줌), .text하면 text만 가져옴
# print(soup.find_all("span", class_="tah")[0].text) # class는 파이썬 문법이 있어서 언더바를 추가해야함(속성값에 띄어쓰기 있으면 둘중 하나만)

# print(soup.find_all("em", class_="no_up")[0].text)


'''
##################################################################
# [CSS Selector]
# soup.select('.class명')
# soup.select('#id명')
# soup.select('태그명') (HTML 태그명은 아무것도 안붙임)
# soup.select('.class명1 .class명2') (띄어쓰기는 '~내부의' 라는 뜻)
##################################################################
'''
# soup.select(".f_up") # css 셀렉터 (class가 .f_down인거 찾기)
# soup.select("#tah") # css 셀렉터 (id가 tah인거 찾기)
# soup.select('strong#_nowvel') # 11번 Line과 같은 코드
# soup.select('.f_down em') # 띄어쓰기 = 내부요소
# print(soup.select('.gray .f_up em')[0].text.strip()) # strip은 공백제거

img = soup.select('#img_chart_area')[0] # 이미지추출
# print(img['src'])

lg = requests.get('https://finance.naver.com/item/sise.naver?code=066570')
soup = BeautifulSoup(lg.content, 'html.parser')

print(soup.find_all("strong", id="_nowVal")[0].text)
print(soup.find_all("span", class_="tah")[0].text)


# 이미지 URL을 알고있을 때 파일로 저장하는 법
# urllib.request.urlretrieve(이미지URL, '파일명')
urllib.request.urlretrieve(img['src'], '삼성전자.jpg')