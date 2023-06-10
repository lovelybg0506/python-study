# 회귀분석 (집값예측)
import numpy as np
import statsmodels.api as sm # 통계분석용 api

# sm.OLS(y,x).fit()  # y = 결과, x = 변수

import pandas as pd
df = pd.read_csv('california_housing.csv')

model = sm.OLS(df['price'], df[['year','rooms','bedrooms']]).fit()
print(model.summary())

a = model.predict([20,1000,200]) # 추정해보기 (20년된 집, 방갯수1000개, 침실200개)
# 여러개 하려면 a = model.predict([20,1000,200], [a1,b1,c1], [a2,b2,c2] ...)
print(a)

'''
가설 : y = ax + b (직선)

R-squared : R제곱값 0~1 사이의 값, 1에 가까울수록 좋은 회귀분석데이터
Prob (F-statistic) : y = ax + b라는 가설을 세웠을때에 a가 0일 확률
AIC : 다른모델과 비교해서 적을수록 좋은 모델

coef  : a값
P>|t| : 적을수록 좋음 (0.05 이하면 이 coefficient가 유의미하다)
[0.025 ~ 0.975] : 신뢰구간

'''