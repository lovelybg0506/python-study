# nunu = {
#     'q' : 'eat',
#     'w' : 'snowball' 
# }

# garen = nunu # 이렇게하면 복사가 아니고 참조(값을 공유함) 이렇게 쓰면 안됨
# char2 = nunu # 딕셔너리형태의 데이터는 함부로 등호사용 X
# char3 = nunu
# char3['q'] = 'adsf'

# Object 생산해주는 기계 = class
class Champion:
    def __init__(self, q, w): # object 생성할때 def __init__ 실행됨
        self.q = q
        self.w = w

    def hello(self):
        print('안녕하세요')

nunu = Champion('eat', 'snowball')
garen = Champion('strike', 'courage')
print(nunu.q)
print(garen.q)
print(nunu.w)
print(garen.w)
nunu.hello()
garen.hello()