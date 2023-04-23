import requests
from bs4 import BeautifulSoup
import datetime as dt # 날짜추가(매일 새로운 파일로 생성해서 쓰려고)

today = dt.datetime.now().strftime("%Y_%m_%d")

# 005930 : 삼성전자
# 035720 : 카카오
# 035420 : 네이버

codeList = ['005930','035720','035420']

def stockCrawling(code):
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={code}')
    soup = BeautifulSoup(data.content, 'html.parser')
    
    # 종목명
    stockName = soup.select('.h_company .wrap_company h2 a')[0].text
    
    # 현재가
    nowPrice = soup.select('strong#_nowVal')[0].text

    # 변동금액
    varAmount = soup.select('strong#_diff .tah')[0].text.strip()
    
    # 2023.04.23 카카오의 변동금액이 0이라서 상승 or 하락 태그가 아예없어서 인덱싱 오류가났음. if로 처리
    if varAmount != '0':
        # 상승 or 하락
        upOrDown = soup.select('strong#_diff .blind')[0].text
    else:
        upOrDown = '변동없음'

    return stockName, nowPrice, varAmount, upOrDown

f = open(f'todayStock_{today}.txt', 'w', encoding='utf-8') # 인코딩 방식 안써줘서 한글 깨졌음
f.write(f"######<{today} 주식>######\n")
f.close()

for i in codeList:
    stockName = stockCrawling(i)[0] # 종목명
    nowPrice = stockCrawling(i)[1]  # 현재가
    varAmount = stockCrawling(i)[2] # 변동금액
    upOrDown = stockCrawling(i)[3]  # 상승 or 하락

    f = open(f'todayStock_{today}.txt', 'a', encoding='utf-8')
    f.write(f"\n<{stockName}>")
    f.write(f"\n현재가   : {nowPrice}")
    f.write(f"\n변동금액 : {varAmount}")
    f.write(f"\n상승,하락 : {upOrDown}")
    f.write("\n")
    f.write("\n============================")
    f.write("\n")
    f.close()
