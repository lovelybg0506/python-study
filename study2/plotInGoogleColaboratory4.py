# 회귀분석 (나이로 소득예측)
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_table('INCOME.txt')
df = df.dropna()

plt.scatter(df['age'],df['income'])
plt.show()

def 함수(x, a, b, c):
  return a*x + b*x**2 + c

opt, cov = curve_fit(함수, df['age'], df['income'])
a,b,c = opt

import numpy as np

x = np.array([1,2,3,4,5,6])
plt.scatter(df['age'],df['income'])
plt.plot(x, 함수(x,a,b,c))
plt.show()

# statsmodel사용해서 Polynomial 분석
import statsmodels.api as sm

# 가설 : y = ax + bx2 + c

# x = np.column_stack([df['age'], df['age']**2], np.ones(79)) # np.ones() : 1을 79개넣어줌
x = np.column_stack([df['age'], df['age']**2]) # 상수항을 삭제하면 R제곱값이 더 늘어남 (더 적합한 예측데이터가 됨)

model = sm.OLS(df['income'], x).fit()
print(model.summary())


'''
overfitting
커브가 너무많아져서?
딱 이 데이터들에만 적합해지는 현상
'''