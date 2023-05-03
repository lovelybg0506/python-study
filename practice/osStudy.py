# 파일 대량 rename, 분류 , 딥러닝 머신러닝, 데이터분석, 웹서버 , 뭘 만들든 많이쓰임

import os # 파이썬으로 PC파일 조작

files = os.listdir('testFolder') # listdir('폴더') : 경로안에 있는 파일명 다 알려주는함수 (리스트형식)
# print(files) # ['1.txt','2.txt','3.txt']

'''
sumtext = 'test_file_'

for i in os.listdir('testFolder'):
    os.rename(f'testFolder/{i}', f'testFolder/{sumtext}{i}') # rename() : 파일명 변경
'''

import shutil # 파이썬으로 파일 복사

for i in os.listdir('testFolder'):
    shutil.copy(f'testFolder/{i}', f'testFolder_2/{i}') # .copy('파일경로FROM', '파일경로TO') : 파일 복사

'''
상대경로 ()

절대경로 (r'C:기준 쭈우욱~~') r을 이용해서 \t 또는 \f 오류 안나도록 쓰기

os.path.join('경로', '경로2') # 경로합쳐줌
경로/경로2
그냥 '경로' + '경로2' 로 써도됨

os.getcwd() # current working directory 현재경로 알려주는 함수

'''