# 정규식 : 문자를 검사하는 식
import re

# re.search('정규식', '테스트할 문자') # 있으면 object, 없으면 None
'''
a = re.findall('a$', 'abcdefg') # re.findall('이글자가','여기에있는지?') # 있으면 [list]에 담아줌
print(a)
'''
# 특수기호 찾으려면 앞에 \ 백슬래쉬 사용
# ^a : a로 시작하냐?
# a$ : a로 끝나냐?
# [abc] : a or b or c를 찾아라
# [a-z] : a~z까지 찾아줘
# [A-Z] : A~Z까지 찾아줘
# [가-힣] : 한글 찾기
# [ㄱ-ㅎ] : 자음 찾기
# [^0-9] : [대괄호 안의 ^표시는 not이라는 뜻] 즉, 0-9가 아닌것
# \d : (숫자)digit의 약자 (모든숫자찾기)
# \d\d : 2자리숫자
# \d\d\d : 3자리숫자
# \d{3} : 왼쪽의것을 3번 곱해라
# \D : ^\d (숫자가아닌 모든 문자)
# \s : 스페이스바 찾기
# \S : 스페이스바 아닌것 찾기 ( 그냥 모든 문자 )
# a+ : +기호 = 반복된거 찾기 즉, a반복되는거 다찾기

# a = re.findall('ㅋ+', 'acdㅁ안ㅁ녕1ㅋㅋㅋㅋㅋㅋㅋ5 42ㄴㅇA ㅋㅋㄹBㅎ하세C141 2D요Fe$f^g', re.IGNORECASE) # re.IGNORECASE : 대소문자 신경안씀
# print(a)



# .sub('a','b','string문장') : string문장의 a를 찾아서 b로 바꿔줘

# a = re.sub('\d','','cdㅁ안ㅁ녕1ㅋㅋㅋㅋㅋ542ㄴㅇAㅋㅋ') # 숫자 제거
# a = re.sub('[^\d]','','cdㅁ안ㅁ녕1ㅋㅋㅋㅋㅋ542ㄴㅇAㅋㅋ') # 문자 제거 (숫자가 아닌것 제거)
# print(a)

'''
quiz1) 이메일형식이 맞는지 판단하는 정규식 만들기
결과 = re.findall('???', 'abc@example.com')
print(결과)
abc@example.com

답)
result  = re.findall('[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+', 'abc@example.com') # [문자,숫자다찾아줘]+(반복기호)@[문자,숫자]+(반복기호).[문자,숫자]+(반복기호)
result2 = re.findall('\S+@\S+.\S+', 'abc@example.com')
print(result)
print(result2)
'''