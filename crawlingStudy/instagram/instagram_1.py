# selenium install : pip install selenium==3.141.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request # 사진저장용 (기본라이브러리)

driver = webdriver.Chrome('chromedriver.exe') # 같은폴더에 있어서 프로그램 파일명만 썼음, 다른폴더일 경우엔 경로를 다 적어줘야함
driver.get('https://instagram.com')

time.sleep(2) # 2초 기다려줘
instagramId = driver.find_element_by_css_selector('input[name="username"]') # 이 selector 찾아줘
instagramPwd = driver.find_element_by_css_selector('input[name="password"]')

instagramId.send_keys('인스타id') # 찾은 selector에 이 값 넣어줘
instagramPwd.send_keys('비번')

instagramPwd.send_keys(Keys.ENTER) # enter 눌러줘
# instagramId.click() # 클릭해줘


# 페이지이동
time.sleep(3)
driver.get('https://www.instagram.com/explore/tags/halland/')

# 첫번째사진 클릭
driver.implicitly_wait(10) # 찾을 요소가 없으면 니가 알아서 최대 10초동안 기다려라
firstPicClick = driver.find_element_by_css_selector('._aagw').click() # 한 페이지에 같은 class가 42개 있는데 사실 맨위의 하나만 찾아주는 함수임 (element)
# firstPicClick = driver.find_elements_by_css_selector('._aagw')[1].click() # (elements) 리스트로 42개 다 가져옴 (클래스명이 중복될경우 사용하자)

'''
# 사진저장
picUrl = driver.find_element_by_css_selector('._aato ._aagv .x5yr21d').get_attribute('src') # 이 요소의 src(이미지주소)
urllib.request.urlretrieve(picUrl, 'halland_1.jpg') # 1.jpg로 저장해줘

# 다음버튼
# nextBtn = driver.find_element_by_css_selector('._abl-').click() # 가끔 클릭이 안먹을때는 아래처럼
nextBtn = driver.find_element_by_css_selector('._abl-')
driver.execute_script('arguments[0].click();', nextBtn) # execute_script = 자바스크립트실행시켜줘 / (javascript문법, 누를거)

# 사진저장2
picUrl = driver.find_element_by_css_selector('._aato ._aagv .x5yr21d').get_attribute('src')
urllib.request.urlretrieve(picUrl, 'halland_2.jpg')
'''

for i in range(10):

    # 사진저장
    picUrl = driver.find_element_by_css_selector('._aato ._aagv .x5yr21d').get_attribute('src')
    urllib.request.urlretrieve(picUrl, f'halland_{i}.jpg')

    # 다음버튼
    nextBtn = driver.find_element_by_css_selector('._abl-')
    driver.execute_script('arguments[0].click();', nextBtn)


# d = driver.find_element_by_css_selector('#어쩌구').text # #id명
# e = driver.find_element_by_css_selector('._aa4u .x1lliihq').text # .클래스명
# f = driver.find_element_by_css_selector('input[name="username"]').text # input태그 쓰는법
# g = driver.find_element_by_css_selector('.LC20lb span').text # span태그 쓰는법 (윗요소의 클래스명 + 띄어쓰기 + 밑요소의 태그명)