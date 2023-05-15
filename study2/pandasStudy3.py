import pandas as pd

raw = pd.read_excel('product.xlsx', engine="openpyxl") # openpyxl 사용하려면 pip install openpyxl

# print(raw)

# df에서 새 컬럼 만들기
# raw['부가세포함가격'] = raw['판매가'] * 1.1

'''
# raw['판매가'].apply(함수) # 특정컬럼에 있는 모든데이터를 함수에 넣었다 빼줌
def vat(a):
    return a * 1.1

print(raw['판매가'].apply(vat))
'''

import re # 정규식

# a = re.search('abc', 'alksacjdhf') # abc가 있냐 (문자찾기) 맞으면 Object형태값 return, 아니면 None
# a = re.search('^abc', 'alksaabccjdhf') # ^abc : abc로 시작하냐

def 함수2(a):

    if re.search('Chair', str(a)): # 정규식과는 글자만 비교가능
        return '의자'
    elif re.search('Table', str(a)):
        return '책상'
    elif re.search('Mirror', str(a)):
        return '거울'
    elif re.search('Sofa', str(a)):
        return '소파'

raw['카테고리'] = raw['상품목록'].apply(함수2)

print(raw)