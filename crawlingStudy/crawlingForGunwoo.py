import requests
from bs4 import BeautifulSoup

url = 'https://www.fmkorea.com/search.php?mid=hotdeal&category=1254381811&listStyle=webzine&search_keyword=5600+4070&search_target=title_content'

# 웹 페이지 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 클래스가 .hotdeal_var8인 요소 찾기
elements = soup.select('.hotdeal_var8')

# 파일을 쓰기 모드로 열기
file_path = "5600x4070.txt"
file = open(file_path, "w")

# 글과 링크 출력
for element in elements:
    # 댓글 수가 있는 span 요소 제거
    for span in element.select('span'):
        span.decompose()
    
    # 글과 링크 출력
    title = element.text.strip()
    link = element['href']
    link = link.replace('/index','https://www.fmkorea.com/search')

    # 파일에 텍스트 작성
    file.write(f'제목: {title} \n')
    file.write(f'링크: {link} \n')
    file.write('-----------------\n')

# 파일 닫기
file.close()