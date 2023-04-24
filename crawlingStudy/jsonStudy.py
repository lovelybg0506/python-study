import requests
import json
import time

# 코인원 사이트의 개발자도구 Network탭에서 Hearders의 RequestURL로 데이터뭉텅이 가져옴
data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone&type=1w')

# json파일(jsonStudy.json)을 만들고,
# 데이터 복붙 + 마우스 우클릭 + Format Document로 이쁘게 정렬가능

# "큰따옴표"형식은 딕셔너리인데, JSON으로 바꿔야 파이썬으로 편하게 조작가능(글자취급을해줌)
dict = json.loads(data.content)

for i in range(200):
    t = dict['data'][i]['DT']
    # 시간이 epoch타입(13자리)이면 나누기 1000 (dict['data'][0]['DT'])
    StringTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t/1000))

    print(StringTime)
    print(dict['data'][i]['Close'])
