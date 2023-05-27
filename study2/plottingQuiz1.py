'''
아마존(종목코드 AMZN) 주식의 2020년 1월 1일~ 12월31일 의 주식가격을 yahoo에서 가져온 후 20일, 60일 이동평균선그리기
'''

import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import yfinance as yf 


# df = data.DataReader('AMZN','yahoo', start="2020-01-01", end="2020-12-31") 오류나서 yfinance로 사용
# print(df['Close'])

df = yf.download('AMZN', start="2020-01-01" , end="2020-12-31") # 위에걸로 하면 오류나서 yfinance 사용

# print(df['Close']) # 확인해보니 이건 이미 float형식이라 astype사용해서 안바꿔줘도될듯

df['rolling20'] = df['Close'].rolling(20).mean() # 20일 평균
df['rolling60'] = df['Close'].rolling(60).mean() # 60일 평균

plt.plot(df.index, df['rolling20']) # 첫번째 선
plt.plot(df.index, df['rolling60']) # 두번째 선
# plt.plot(df.index, df['Close']) # 세번째 선
plt.xlabel('time')
plt.ylabel('price')
plt.legend(['20days','60days','Close'])
plt.title('movingAverage')
plt.show()