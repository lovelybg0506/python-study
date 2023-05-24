import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt # python에서는 이거쓰는듯

'''
# data.DataReader() # yahoo finance, naver finance에서 가져올수있음 (비트코인도 가능)
df = data.DataReader('005930', 'naver', start="2019-01-01", end="2020-01-01")
# df = df['Close']         # 종가
# df = df.index            # 날짜만나옴(Index)
# df = df['Close'].plot()  # Colaboratory에서는 이거 사용하면 그래프나옴

# df = df['Close']           # dtype : object

df['Close'] = df['Close'].astype(float) # dtype : float로 바꾸기
df = df['Close']

# 파이썬에서는 이거써야 그래프나오는듯 (시계열데이터 : time series 시간을기준으로 시각화한 데이터)
plt.plot(df)
plt.show()
'''
###################################################################################################
'''
[이동평균선]
n일간 가격을 평균내서 그래프로 그린 것
'''
df = data.DataReader('005930', 'naver', start="2019-01-01", end="2020-01-01")

df['Close'] = df['Close'].astype(float) # dtype : float로 바꾸기
df['rolling5'] = df['Close'].rolling(5).mean() # 5일 평균
df['rolling20'] = df['Close'].rolling(20).mean() # 20일 평균

# plt.plot(df)
# plt.show()