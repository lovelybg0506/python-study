import pandas as pd

df = pd.read_csv('credit.csv') # 경로 (같은위치라서 파일명만 적음)
# print(df)
# 원하는 세로줄 출력
# print(df['나이'].mean()) # .mean() : 평균
# print(df['나이'].mode()) # .mode() : 최빈값
# print(df['나이'].max())  # .max()  : 최대값
# print(df['나이'].min())  # .min()  : 최소값
# print(df['나이'].describe())  # .describe()  : 통계
# print(df[['사용금액','사용횟수']].describe()) # 컬럼 두개 세개를 동시에 추력하려면 리스트형식으로 넣으면됨 []안에 []

# df : 판다스에서 다루는 dataframe 자료형 (가로세로, 행과 열이 있는 데이터형)
# Series : 판다스에서 쓰는 한줄 데이터 형식 (=리스트형식)

# print(df.groupby('성별').mean())

# print(df[['나이','사용금액']].corr()) #correlation값 구하기 # 1과 가까울수록 관련있다

# 원하는 데이터만 필터링
# df[ df['나이'] > 50 ] # 조건식
# a = df.query(" 나이 > 50 and 기혼 == 'Married' ") # 문자자료는 따옴표써주기
# print(a)


##################################################################
# 기존 list데이터를 dataframe형식으로 변환
shirts = [15, 20, 25]
pants = [150, 160, 170]

dictionary = {
    'shirtsData' : shirts,
    'pants' : pants
}

df2 = pd.DataFrame(dictionary)
print(df2)
##################################################################