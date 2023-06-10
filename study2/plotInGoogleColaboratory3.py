# 회귀분석 (나이로 소득예측)
from scipy.optimize import curve_fit # curve_fit : 곡선그릴때 사용
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table('INCOME.txt')
df = df.dropna() # NaN 이 들어있는 데이터 (행)삭제

plt.scatter(df['age'],df['income'])
plt.show()

def 함수(x, a, b, c):
  return a*x + b*x**2 + c  # **은 제곱임

opt, cov = curve_fit(함수, df['age'], df['income']) # curve_fit() 실행하면 그자리에 데이터 2종 남음
a,b,c = opt

import numpy as np

x = np.array([1,2,3,4,5,6]) # .array() : list를 array로만들어줌 수학 행열 계산할때 array사용

plt.scatter(df['age'], df['income'])
plt.plot(x, 함수(x, a, b, c))
plt.show()
