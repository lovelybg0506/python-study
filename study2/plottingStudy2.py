import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

# plt.plot([1,2,3],[4,5,6]) # plt.plot([x축], [y축]) 
# plt.show()

df = data.DataReader('005930', 'naver', start="2023-05-01", end="2023-05-23") # 네이버에서 가져온 삼성전자주식
df2 = data.DataReader('035420', 'naver', start="2023-05-01", end="2023-05-23") # 네이버에서 가져온 네이버주식

# 차트 시각화
'''
plt.plot(df.index, df['Close'], color="crimson")
plt.xlabel('time')      # x축 이름
plt.ylabel('price')     # y축 이름
plt.legend(['SamSung'])   # 선의 이름? (선이 여러개일때는 ['legend1','legend2' ...])
plt.title('Samsung Chart From NaverFinance')    # 차트 이름 (한글은 안됨)
plt.show()

print(df['Close'])
'''

# bar 차트 (보통 가로축 데이터가 적을때 bar차트 사용)
'''
plt.bar(df.index, df['Close'])
plt.show()
'''

# pie 차트 (이 항목이 몇% 차지하고있는지 알고싶을때) 이건 데이터가 한종류밖에 안들어감
'''
plt.pie([57,35,11], labels=['ramen', 'tuna', 'snack']) # pie('','')
plt.show()
'''

# histogram (어떤 값이 빈출한지, 분포는 어떤지)
'''
plt.hist([160,165,170,171,172,180])
plt.show()
'''

# scatter plot (두 데이터가 관계가있는지?)
'''
math = [5,8,23,5,67,34,34,23] # 위 아래 데이터 수가 같아야함
eng = [23,6,3,1,5,45,54,34]

plt.scatter(math,eng)
plt.show()
'''

# stackplot (누적 그래프) y축데이터가 여러개 들어감 .stackplot(x축데이터, y축데이터, y축데이터2 ...)
'''
plt.stackplot([1,2,3], [10,20,30], [30,20,50], [10,20,10])
plt.show()
'''

# 여러 선을 한 차트에 띄우려면 plot 하나당 선 하나인듯
'''
plt.plot(df.index, df['Close']) # 첫번째 선
plt.plot(df2.index, df2['Close']) # 두번째 선
plt.show()
'''

plt.figure(figsize=(20,10)) # 크기 키우기 (인치사이즈) 이런 세부설정은 그냥 필요할때 찾아쓰자
plt.plot(df.index, df['Close']) # 첫번째 선
plt.plot(df2.index, df2['Close']) # 두번째 선
plt.xlabel('time')
plt.ylabel('price')
plt.legend(['SamSung','Naver'])
plt.title('SamSung And Naver DailyClosePrice From NaverFinance In May')
plt.show()