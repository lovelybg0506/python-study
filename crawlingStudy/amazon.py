import requests

'''
아마존 -> F12(개발자도구) -> Network 탭 -> 제일 첫번째 파일의 Headers - > Request Headers (나의 접속정보)
여기에 user-agent라는게 있는데 이게 정상적이지 않으면(파이썬?이면) 차단
user-agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
'''

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

ck = {'session-id' : '136-9910747-8076230',
          'session-id-time' : '2082787201l',
          'i18n-prefs' : 'USD',
          'sp-cdn' : 'L5Z9:KR',
          'skin' : 'noskin',
          'ubid-main' : '134-5275088-7891010',
          'lc-main':'ko_KR',
          'session-token':'HobB7gpzz8NnIsuCYqUrpFTGlVbx36apDhhxosEvQaJ92HUgb8WgsR9EIit8a7/csekiUUAZzzTG3MZ5PCXajXmw4PURjd4145kxtNAiqmsZ/fyuUg7Rw7EUbCLOV1gCoMUTHdOYMWMH7YGl8vDjE8C6/S6Rfljb+8GnibcQ2SJbU8Tafgw2e0R9AoB5IHf9Z3yzZQVQGPvv83mY0a7LdK+KjqZ5SjVyAwbMRQVktTs=',
          'csm-hit' : 'tb:S54T6VDY8XNDCP8PT55F+s-F8C80CPF09W2PTDFWPS8|1683468254078&t:1683468254078&adb:adblk_no'
}

r = requests.get('https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2', headers=hd , cookies=ck) # 헤더와 쿠키 정보를 입력해주면 아마존에서 정상적인 경로로 들어온줄 알음(뚫기성공)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'lxml')
# print(soup.select('.a-size-medium')[0])

#에러나서 코드가 멈추는걸 예방
'''
# 1번
if r.status_code == 200: # 200일때
    print(soup.select('.a-size-medium')[0]) # 수집
else:
    print('Error : statusCode is not 200')

# 2번
try:
    print(soup.select('.a-size-medium')[110]) # 에러나면
except:
    print('에러났지만 다음거 계속')

'''

# print(r.content)
# print(r.status_code) # status_code가 503으로 나오면 서버에서 이 연결을 차단한것. (4XX, 5XX : 오류)