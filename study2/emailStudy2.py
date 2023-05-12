import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

text = "메일 내용입니다"
msg = MIMEMultipart()
msg['Subject'] ="이것은 메일제목"
msg['From'] = 'lovelybg0506@naver.com'
msg['To'] = '받는자이메일또는이름'
msg.attach(MIMEText(text))
print(msg.as_string())

#원하는 파일 rb로 오픈
with open('images/photo1.jpg', 'rb') as file: # 보낼파일경로 , 'rb'
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(file.read())

#파일 base64 인코딩
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="photo1.jpg"')
msg.attach(part)

s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls()
s.login( 'lovelybg0506' , '비번' ) # 네이버 아이디, 비번 
s.sendmail( 'lovelybg0506@naver.com', 'lovelybg0506@naver.com', msg.as_string() )  # 보내는사람, 받는사람
s.close()