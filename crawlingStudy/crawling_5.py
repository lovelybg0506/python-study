import requests
import json
import time

# 멀티 쓰레딩 사용하기(병렬작업)

url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def Price(a): 
    data = requests.get(a)
    dict = json.loads(data.content)
    return {
           "Price" : dict['data'][0]['Close'], 
           "Time"  : dict['data'][0]['DT']
           }

# 멀티프로세싱 : 여러개의 파이썬 실행창 띄우기
# 멀티쓰레딩 : CPU 병렬처리

# Price(url[0])

'''
map 함수 (내장함수)
리스트 자료에 똑같은 작업을 하고싶다면 사용

List = [2,3,4,5,6]
def sumFunc(x):
    return x+1

map(sumFunc, List) 이렇게 쓰면 [3,4,5,6,7]

'''


from multiprocessing.dummy import Pool as ThreadPool # .dummy 까지 쓰면 멀티쓰레딩을 할수있음. 
                                                     # (multiprocessing까지만 쓰면 멀티프로세싱 라이브러리)

pool = ThreadPool(4) # 몇개의 쓰레드를 동시에 띄울지
result = pool.map(Price, url)
pool.close() # 닫기
pool.join() # 결과가 나올때까지 기다려라 (.close와 .join은 같이 쓰임)

print(result)
print(result[0])
print(result[0]['Price'])
print(result[0]['Time'])
