import requests
from bs4 import BeautifulSoup

# cList = []

# 005930 삼성전자
# 066570 LG전자

def crawling(code):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={code}')
    soup = BeautifulSoup(data.content, 'html.parser')
    print(soup.find_all("strong", id="_nowVal")[0].text) # 현재가
    print(soup.find_all("span", class_="tah")[5].text)   # 거래량
    # cList.append(soup.find_all("strong", id="_nowVal")[0].text)
    return soup.find_all("strong", id="_nowVal")[0].text

# crawling('005930')
# crawling('066570')

'''
f = open('a.txt', 'w')
f.write(crawling('005930'))
f.write(crawling('066570'))
# f.write(cList[0])
# f.write(cList[1])
f.close()
'''

#         삼성전자, LG전자,   현대차,    카카오,  LG디스플레이, 대한항공
aList = ['005930', '066570', '005380', '035720', '034220', '003490']

f = open('price.txt', 'w')
for i in aList:
    f.write("\n"+crawling(i))
f.close()