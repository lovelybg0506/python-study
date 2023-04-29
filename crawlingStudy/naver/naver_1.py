from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip # 복사도와주는 lib

from selenium.webdriver.chrome.options import Options # 실제 브라우저처럼 꾸미기

# C:\Program Files\Google\Chrome\Application\chrome.exe is no longer running 이오류는 크롬창을 다 닫고 다시실행하면 해결됨

# 계정정보 ("chrome://version/"에서 프로필경로 가져오기)
opt = webdriver.ChromeOptions()
opt.add_argument(r'user-data-dir=C:\Users\lovel\AppData\Local\Google\Chrome\User Data\Default') # r = for slash

# naver 로그인창
# driver = webdriver.Chrome('chromedriver.exe', chrome_options=opt) # 이렇게 썼더니 계속 오류나서 크롬드라이버 절대경로 지정해서 오류해결
driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe', chrome_options=opt)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')

# 그냥 아이디 입력이 아니라 ctrl+v로 아이디입력 (캡쳐검증 방지?)
time.sleep(2)

pyperclip.copy('네이버아이디') # Ctrl + c 아이디

e = driver.find_element_by_css_selector('#id') # 네이버로그인창의 id창 id
# e.send_keys('lovelybg0506') # 이렇게하면 아이디 입력이 너무 빠르다고 인지하고 자동입력방지 문자(사람인지확인) 입력하게함
e.send_keys(Keys.CONTROL, 'v') # Ctrl + v 키 입력 (이런식으로 Ctrl + c,v 를 이용하면 우회가능)

time.sleep(2)
pyperclip.copy('네이버비번')
e = driver.find_element_by_css_selector('#pw')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(2)
e.send_keys(Keys.ENTER)
