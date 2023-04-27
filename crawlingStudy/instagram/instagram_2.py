from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains # 더블클릭함수가 안먹어서 추가함
import time
# import urllib.request # 사진저장용 (기본라이브러리)

driver = webdriver.Chrome('chromedriver.exe') # 같은폴더에 있어서 프로그램 파일명만 썼음, 다른폴더일 경우엔 경로를 다 적어줘야함
driver.get('https://instagram.com')

time.sleep(2) # 2초 기다려줘
instagramId = driver.find_element_by_css_selector('input[name="username"]') # 이 selector 찾아줘
instagramId.send_keys('instaId') # 찾은 selector에 이 값 넣어줘

instagramPwd = driver.find_element_by_css_selector('input[name="password"]')
instagramPwd.send_keys('instaPwd')

instagramPwd.send_keys(Keys.ENTER) # enter 눌러줘
time.sleep(10)

# 페이지이동
driver.get('https://www.instagram.com/상대 인스타주소/')

# 테스트하느라 로그인 너무 많이해서그런가 갑자기 로그인막힘 그래서 밑에 테스트 하다가 끊김;
# Instagram에 연결할 수 없습니다. 인터넷에 연결되어 있는지 확인한 후 다시 시도해보세요.


# 첫번째 사진클릭
driver.implicitly_wait(10)
driver.find_element_by_css_selector('._aagw').click()

for i in range(60): # 70~75개?? 넘어가니까 '나중에 다시 시도하세요' 라며 인스타에서 막음.
    driver.implicitly_wait(10)
    # driver.find_element_by_css_selector('._aatk').double_click() # 사진 더블클릭 (이렇게쓰니까 계속 오류남)
    # photo = driver.find_element_by_css_selector('._aatk')
    # video = driver.find_element_by_css_selector('div[role="presentation"]')

    # actions = ActionChains(driver)
    # actions.move_to_element(photo).double_click().perform() # 사진 더블클릭(ActionChains를 쓰니까 오류해결)
    driver.find_element_by_css_selector('._aamw').click() # 좋아요버튼
    driver.find_element_by_css_selector('._aaqg ._abm0').click() # 다음버튼

    # 사진이 아닌 동영상인경우에는 더블클릭을 하면 동영상이 일시정지 후 다시재생 되고있음 (버림) 걍 쉽게가자
    # try:
    #     torf == True
    # except:
    #     print("4번")
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_css_selector('._aamw').click() # 좋아요버튼 (동영상일경우에는 좋아요버튼으로)
    #     driver.find_element_by_css_selector('._aaqg ._abm0').click() # 다음버튼
