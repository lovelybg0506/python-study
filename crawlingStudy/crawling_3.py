import requests
from bs4 import BeautifulSoup

# 무한스크롤 (start : 시작점?, query : 검색어 %EC%82%AC%EA%B3%BC == '사과')
data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=61&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=62&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09290122&fgn_region=&fgn_city=&lgl_lat=37.586732&lgl_long=127.023&abt=&_callback=viewMoreContents')

# soup = BeautifulSoup(data.content.replace('\\',''), 'html.parser') # html parsing해주기(해석해주기), # class같은곳에 백슬래쉬'\' 가 들어가있는경우 제거해줘야함
soup = BeautifulSoup(data.text.replace('\\',''), 'html.parser') # 위처럼 content는 String타입이 아니라서 .replace가 안됨. 그럴땐 .text로 쓰자

gList = soup.select('a.api_txt_lines')
print(gList[0].text) # a태그 안의 text만 뽑아옴
print(gList[1].text)
print(gList[2].text)
print(gList[0]['href']) # a태그 안의 href(주소)
print(gList[1]['href'])
print(gList[2]['href'])