from papago3 import translation

'''
ko : 한국어
en : 영어
ja : 일본어
zh-CN : 중국어(간체)
zh-TW : 중국어(번체)
es : 스페인어
fr : 프랑스어
de : 독일어
ru : 러시아어
pt : 포르투갈어
it : 이탈리아어
vi : 베트남어
th : 태국어
id : 인도네시아어
hi : 힌디어
'''

content = '표준잔가율'

a = translation(content, 'ko', 'en')

print(a)