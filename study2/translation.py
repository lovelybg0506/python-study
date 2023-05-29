from papago3 import translation
import pandas as pd

data = pd.read_excel('english.xlsx', engine='openpyxl') # 판다스 이용해서 엑셀파일 읽기

# print(data['english'][0]) # english열의 0번째 행

# l : 행의 번호
# row : 영어문장
for l, row in data.iterrows(): # iterrows() : list형식
    data.loc[l, 'korean'] = translation(row['english']) # data.loc[행,열] : pandas에서 데이터수정
    
data.to_excel('koreanTranslate.xlsx') # excel로 만들기
data.to_csv('koreanTranslate.csv')    # csv로 만들기