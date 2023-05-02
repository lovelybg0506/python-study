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
driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')

time.sleep(2)

img = driver.find_element_by_xpath('/html/body/form/input[1]')
img.send_keys('C:/Users/lovel/OneDrive/Desktop/mine/ManchesterCity.jpg')
# img.send_keys(r'C:\Users\lovel\OneDrive\Desktop\mine\ManchesterCity.jpg')
