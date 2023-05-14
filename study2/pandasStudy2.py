import pandas as pd

df = pd.read_csv('credit.csv')

# df[ ['나이','사용금액'] ].corr() #correlation

# df[ df['나이'] > 50 ]


'''
# 남자고 결혼한사람은 사용금액의 평균이 높을까? (남자고 결혼하지않은사람보다)
df2 = df.query(" 성별 == 'M' and 기혼 == 'Married' ")
df3 = df.query(" 성별 == 'M' and 기혼 == 'Single' ")

print(df2['사용금액'].mean())
print(df3['사용금액'].mean())

quiz1 = bool(df2['사용금액'].mean() > df3['사용금액'].mean())
print(quiz1)
'''

'''
# 소득이 많을수록 사용금액이 높을까?
# df.groupby('소득').mean()
'''

