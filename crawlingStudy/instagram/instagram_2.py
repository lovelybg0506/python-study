from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request # 사진저장용 (기본라이브러리)

driver = webdriver.Chrome('chromedriver.exe') # 같은폴더에 있어서 프로그램 파일명만 썼음, 다른폴더일 경우엔 경로를 다 적어줘야함
driver.get('https://instagram.com')

time.sleep(2) # 2초 기다려줘
instagramId = driver.find_element_by_css_selector('input[name="username"]') # 이 selector 찾아줘
instagramPwd = driver.find_element_by_css_selector('input[name="password"]')

instagramId.send_keys('InstaId') # 찾은 selector에 이 값 넣어줘
instagramPwd.send_keys('pwd')

instagramPwd.send_keys(Keys.ENTER) # enter 눌러줘
time.sleep(3)

# 페이지이동
ujh = driver.get('https://www.instagram.com/instagramSomeoneId/')

# 테스트하느라 로그인 너무 많이해서그런가 갑자기 로그인막힘 그래서 밑에 테스트 하다가 끊김;
# Instagram에 연결할 수 없습니다. 인터넷에 연결되어 있는지 확인한 후 다시 시도해보세요.


# 첫번째 사진클릭
driver.implicitly_wait(10)
driver.find_element_by_css_selector('._aagw').click()

for i in range(50):
    time.sleep(1)
    driver.find_element_by_css_selector('._aato').double_click() # 사진 더블클릭
    driver.find_element_by_css_selector('._aaqg ._abm0').click() # 다음버튼

