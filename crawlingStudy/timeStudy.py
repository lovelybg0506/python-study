import time

# a = time.time() # Epoch타입

# # 처리시간이 오래걸리는 코드 ~
# 10000000000000000 + 111111111111111

# b = time.time()
# print(b-a)

a = time.time()
a = time.ctime(a) # ctime = 사람이 볼때 편한 format (요일 월 일 시간:분:초 년도)
print(a)

# localtime() 으로 세부항목만 출력가능
a = time.localtime()
print('현재년도 : ' + str(a.tm_year))
print(a.tm_hour)

# strftime() 으로 시간표시형식 마음대로 format 가능
# time.strftime('포맷팅문법', 로컬타임)
b = time.strftime('%Y year %m month', time.localtime())
print(b)

name = 'Kim'
print('안녕하세요 %s'%name)
print(f'안녕하세요 {name}')
print('안녕하세요 {}'.format(name))

import datetime
ab = datetime.datetime(2022, 10, 1, 12 ,12, 30)
print(ab)

nowtime = datetime.datetime.now()
print(nowtime)

print(f'''
이렇게 쓰면{ab}
어떻게
될
까
요
?{nowtime}
''') # 쓴대로 나옴 (줄바꿈포함)

print('--------시간을 다시 epoch형태로 되돌려보고싶은데?-----------')
ts = datetime.datetime(2023, 4, 24, 22, 26, 00)
print(ts)
ts = datetime.datetime(2023, 4, 24, 22, 26, 13).timestamp() # 시간을 epoch 타입으로
print(ts)
# 다시 시간으로
aaa = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)) # localtime에 아무것도 안넣으면 현재시간, epoch타입 시간 넣으면 formatting해줌.
print(aaa)

# 1682342760.0
# 1682342760.0
# 1682342773.0
# 1682342773000