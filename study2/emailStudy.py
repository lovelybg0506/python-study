# SMTP 
# 메일을 주고받을때 SMTP에 따라 주고받음 (통신규약)
# SMTP 서버를 만들어야함 네이버같은 곳에서 지원해줌

# 복붙한거임
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart('alternative')
내용 = """
여기에 HTML로 작성가능
<h4>굵은제목</h4>
<button>버튼</button>
"""
part1 = MIMEText(내용, "html")
msg.attach(part1)

# text = "메일 내용입니다123"
# msg = MIMEText(text) 
 
msg['Subject'] ="이것은 메일제목"
msg['From'] = 'lovelybg0506@naver.com' # 보내는사람 이메일
msg['To'] = '받는 자' # 받는사람
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) # SMTP서버, 포트번호
s.starttls() #TLS 보안 처리
s.login( 'lovelybg0506' , '비번' ) #네이버로그인 (아이디, 비번)
s.sendmail( 'lovelybg0506@naver.com', 'lovelybg0506@gmail.com', msg.as_string() ) # 발신자, 수신자 (gmail은 스팸함에 들어있었다)
s.close()