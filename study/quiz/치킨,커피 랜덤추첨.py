'''
문제)
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample 활용

(출력 예제)
-- 당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
shuffle(lst)
sample(lst,1)
'''


# 내가 푼 방식
'''
from random import *

chicken = 0
coffee = []
user = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

user = set(user)
chicken = sample(user,1)
coffee = sample(user,3)


print(f'-- 당첨자 발표 --')
print(f'치킨 당첨자 : {chicken}')
print(f'커피 당첨자 : {coffee}')
print(f'-- 축하합니다 --')
'''

# 정답
'''
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users)) # range Type
users = list(users)
# print(type(users))# list Type으로 바뀜

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중 1명은 치킨, 3명은 커피
print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:])) # winners list의 1,2,3번 Index
print('-- 축하합니다 --')
'''

# 문제풀이 보고 다시 한번 해봄
from random import *

user = range(1,21) #-> 1부터 20까지 숫자를 그냥 생성만해준다
# print(user) -> 여기에서 user찍었을때 그냥 range(1,21) 라고만 찍힘

user = list(user) # 형변환을 해줘야 list형식의 숫자 20개가 찍힘
print(user)

shuffle(user) # 숫자 20개를 섞어줌 그리고 list(대괄호 쓰는배열)형식만 shuffle쓸 수 있음 set, tuple일때 오류남

winners = sample(user,4) # 이중에서 4명만 뽑을것(어차피 랜덤이라 치킨1명뽑고 남은 19개숫자중에 3명 뽑을 필요가없었음)

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {}'.format(winners[0])) # 당첨자 중 0번째 Index값
print('커피 당첨자 : {}'.format(winners[1:])) # 당첨자 중 1번째 Index 부터 끝까지 (당첨자의 length는 4)
print('-- 축하합니다 --')