# 퀴즈) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작서하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

# random, 5~ 15 if, for continue,break

'''
from random import *
cnt = 0 # 총 탑승 승객 수
customer = range(1,51) # 손님 수
print(customer) # 이렇게 찍으면 그냥 range(1,51)이라고만 나옴 1~50까지 찍히지않음
# customer = list(customer) 없어도됨 (range타입이라 for문에서 오류나는줄알았는데 아님 상관없음 == 리스트타입으로 굳이 안바꿔줘도됨)
# time = randrange(5, 51)  여기서 쓰면안되고 for문 안에서 돌려야함

for i in customer:
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 승객 수 : {}".format(cnt))
'''
'''
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))
'''