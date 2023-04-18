
# # # print('풍선'*9) # 이게되네


# # # # 참 / 거짓
# # # print(5>10)
# # # print(False)
# # # print(not True)

# # # print(not (5>10))

# # # 애완동물을 소개해 주세요
# # '''
# # animal = "강아지"
# # name = "크림이"
# # age = 11
# # hobby = "산책"
# # is_adult = age >= 10

# # print("우리집 "+ animal +"의 이름은 " + name + "예요")
# # hobby = "공놀이"
# # print(name, "는 ", str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
# # print(name + "는 어른일까요?" + str(is_adult))
# # '''

# # '''Quiz
# # station = "사당"
# # print(station + "행 열차가 들어오고 있습니다.")

# # station = "신도림"
# # print(station + "행 열차가 들어오고 있습니다.")

# # station = "인천공항"
# # print(station + "행 열차가 들어오고 있습니다.")
# # '''
# # '''
# # print(2**3) # 2 ^3
# # print(5%3) # 나머지값
# # print(10%3)
# # print(5//3) # 몫

# # print(4 >= 8)
# # print(10 < 3)
# # print(5<=5)

# # print(3 == 3)

# # print(4 == 2)
# # print(3 + 4 == 7)

# # print (1 != 3) # not
# # print (not(1!=3))

# # print((3>0) and (3<5))
# # print((3>0) & (3<5))

# # print((3>0) or (3<5))
# # print((3>0) | (3<5)) 

# # print(pow(4,2) == (4**2))
# # '''

# # # from random import *

# # # StudyDay = randint(4,28)

# # # print('오프라인 스터디 모임 날짜는 매월' + str(StudyDay) + '일로 선정되었습니다.')


# # # sentence = '나는 소년입니다'
# # # print(sentence)

# # # sentence2 = "파이썬은 쉬워요"
# # # print(sentence2)

# # # sentence3 = """
# # # 나는 소년이고,
# # # 파이썬은 쉬워요
# # # """

# # # print(sentence3)


# jumin = "960506-1023515"

# # # print("성별 : " + jumin[7])
# # # print("연 : " + jumin[0:2])
# # # print("월 : " + jumin[2:4])
# # # print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])
# print("뒷자리 : " + jumin[7:])
# print("뒷자리부터 : " + jumin[-7:])

# # # python = "Python is Amazing"
# # # print(python.lower())
# # # print(python.upper())
# # # print(python[0].isupper())
# # # print(len(python))
# # # print(python.replace("Python", "Java"))

# # # index = python.index("n")
# # # print(index)

# # # index = python.index("n", index + 1)
# # # print(index)

# # # print(python.find("Java")) # -1
# # # # print(python.index("Java")) # error (find와 index의 차이점)

# # # print(python.count("n"))

# # # print("a" + "b")
# # # print("a","b")

# # # 방법1
# # # print("나는 %d살입니다." % 20) # d = Int
# # # print("나는 %s을 좋아해요." % "파이썬") # s = String 문자열
# # # print("Apple 은 %c로 시작해요." % "A") # c = char 문자

# # # print("나는 %s살입니다." % 20) # d = Int

# # # print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# # # 방법 3
# # # print("나는 {}살이며, {}색을 좋아해요".format(age =20, color="빨간"))

# # # 방법 4 (3.6이상~)
# # # age = 20
# # # color = "검정"

# # # print(f"나는 {age}살이며, {color}색을 좋아해요")

# # # 탈출문자?
# # # 
# # # \n(줄바꿈)

# # # print("백문이 불여일견 \n백견이 불여일타")


# # # 저는 "bgkang"입니다.
# # # print("저는 'bgkang'입니다.")
# # # print('저는 "bgkang"입니다.')
# # # print("저는 \"bgkang\"입니다.")
# # # print("저는 \'bgkang\'입니다.")

# # # \\ : 문장 내에서는 \
# # # print("경로 : "+"C:\\Users\\lovel\\OneDrive\\Desktop\\PythonWorkspace>")

# # # \r : 커서를 맨 앞으로 이동
# # # print("Red Apple\rPine")

# # # /b : 백스페이스 ( 한글자 삭제)
# # # print("Redd\bApple")

# # # \t : 탭
# # # print("Red\tApple")

# # # address = "http://naver.com"
# # # address = "http://daum.net"
# # # address = "http://google.com"

# # # my_address = address.replace("http://","")
# # # my_address = my_address[:my_address.index(".")]

# # # password = my_address[:3] + str(len(my_address)) + str(my_address.count("e")) + "!"

# # # print("{0}의 비밀번호는 {1}입니다.".format(my_address,password))

# # # 리스트 []

# # # subway1 = 10
# # # subway2 = 20
# # # subway3 = 30

# # # subway = [10,20,30]

# # # print(subway[0])

# # # subway = ["유재석", "조세호", "박명수"]
# # # # print(subway.index("조세호")) # 1
# # # # print(subway[2/]) # 박명수

# # # subway.append("하하")
# # # print(subway)

# # # subway.insert(1,"정형돈")
# # # # print(subway)


# # # # print(subway.pop())
# # # # print(subway.pop())
# # # # print(subway.pop())
# # # # print(subway)

# # # subway.append("유재석")
# # # print(subway)
# # # print(subway.count("유재석"))

# # # num_list = [5,2,4,3,1]
# # # num_list.sort()
# # # print(num_list)

# # # num_list.reverse()
# # # print(num_list)

# # # num_list.clear()
# # # print(num_list)

# # # num_list = [5,2,4,3,1]
# # # mix_list = ["강병규", 20, True]

# # # print(mix_list)

# # # num_list.extend(mix_list)
# # # print(num_list)


# # cabinet = {3:"유재석", 100:"김태호"}

# # # print(cabinet[3])
# # # print(cabinet[100])

# # # print(cabinet.get(3))

# # # print(cabinet.get(5,"사용가능")) #5번키에 값이 없으면 사용가능 출력

# # print(3 in cabinet) # true or false
# # print(5 in cabinet) # 키에 값이 있는지 없는지 체크

# # cabinet = {"A-3":"유재석", "B-100":"김태호"}

# # print(cabinet["A-3"])

# # cabinet["A-3"] = "김종국"
# # cabinet["C-20"] = "조세호"

# # print(cabinet)

# # # key값은 Int로 써도되고, String으로 써도 된다.

# # del cabinet["A-3"]
# # print(cabinet) # 값만 삭제되는게아니고 key도 같이지워짐

# # # key들만 출력
# # print(cabinet.keys())
# # print(cabinet.values())

# # print(cabinet.items())

# # cabinet.clear()

# # print(cabinet)



# # 튜플?

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])


# # name = "김종국"
# # age = "20"
# # hobby = "운동"

# (name,age,hobby) = ("김종국",20,"코딩")
# print(name, age, hobby)

#집합(set)
# 중복안됨, 순서 X

# my_set = {1,2,3,3,3} # 중복값 3은 하나만 나옴
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

#교집합 (java, python 교집합)
# print(java & python) == print(java.intersection(python))

# 합집합
# print(java | python) == print(java.union(python))

# 차집합 (java 가능, python 불가능)
# print(java-python) == print(java.difference(python))

# add
# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# 1 치킨
# 3 커피


# from random import *

# user = range(1,21) #-> 생성만해줌
# # print(user) -> 여기에서 찍었을때 그냥 range(1,21) 라고만 찍힘

# user = list(user) # 형변환을 해줘야 list형식의 숫자 20개가 찍힘
# print(user)

# shuffle(user) # 숫자 20개를 섞어줌 

# winners = sample(user,4)     # 이중에서 4명만 뽑을것

# print('-- 당첨자 발표 --')
# print('치킨 당첨자 : {}'.format(winners[0])) # 당첨자 중 0번째 Index값
# print('커피 당첨자 : {}'.format(winners[1:])) # 당첨자 중 1번째 Index 부터 끝까지 (당첨자의 length는 4)
# print('-- 축하합니다 --')


# weather = input("오늘 날씨는 어때요?")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨")
# elif 0 <= temp < 10:
#     print("좀 추워요")
# else:
#     print("너무 추워요 영하기온!")

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1,11):
#     print("대기번호 : {}".format(waiting_no))

# starbuks = ["아이언맨", "토르", "그루트"]

# for customer in starbuks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5

# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 버려졌습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# absent = [2, 5] # 결석한 학생
# no_book = [7] # 책을 안가져온 학생

# for student in range(1,11): # 1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(no_book))
#         break

#     print("{0}, 책을 읽어봐".format(student))

# 출석번호 1 2 3 4, 앞에 100을 붙이기로함 -> 101,102,103,104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# 걍 해봄 근데 첫 프린트문에 들여쓰기가 안되어있어서 오류가났었음 ( 파이썬은 들여쓰기에 주의해야함 )
# for gugu in range(2,10):
#     for dan in range(1,10):
#         print("구구단 {0}단 : {1} * {2} = {3}".format(gugu, gugu, dan, gugu*dan))
#         if dan == 9:
#             print("구구단{0}단 끝".format(gugu))

# from math import *

# # print(sqrt(81))

# from random import *
# a = random()

# print('''
# hi
# hi
# hi
# \'hi\'
# ''')

# def open_account():
#     print("새로운 계좌 생성.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money

# # balance = 0 # 기존잔액
# # balance = deposit(balance,1000)

# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다 잔액은 {0}원 입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금불가 ! (금액부족) 현재잔액은 {0}원 입니다. \n출금신청한금액 : {1}".format(balance,money))
#         return balance
    
# balance = 0# 잔액

# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 3000)

# def withdraw_night(balance, money): #저녁에 출금
#     commision = 100 # 수수료 100원
#     return commision, money - 50

# commision, balance = withdraw_night(balance, 500)

# print("balance : {}".format(balance))

# # print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commision,balance))

'''
# 전역변수 ("global" 사용)

gun = 10 # 전역변수

def checkpoint(soldiers): # 경계근무
    global gun # 전역공간에 있는 gun 사용 (만약 이 문장이 없으면 아랫라인의 gun을 인식하지 못함)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

'''

# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint_ret(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# print("Python", "Java", "JavaScript", sep=" vs ") # sep는 문자열과 문자열 사이에 넣을 값을 정할수있다.(int는 안됨!)

# print("Python", "Java", "JavaScript", sep=" vs ", end="?") # end 는 아래의 두 문장을 한줄로 합침 + 마지막에 넣을문자정함
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력 처리
# print("Python", "Java", file=sys.stderr) # 표준에러 처리 (로그처리시 사용)

# 시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # key와 value를 튜플로 보내줌
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # 왼쪽정렬, 총 8칸의 공간확보 후 정렬 / 오른쪽정렬, 총 4칸의 공간확보

# 은행 대기순번표
# 001 002 003 ...
# for num in range(1,21): # (1~20)
    # print("대기번호 : " + str(num).zfill(3)) # .zfill = 빈공간에 0을 채움

# answer = input("아무 값이나 입력하세요 : ")   # 입력값 input()/
# print(type(answer)) # 숫자를 적어도 자기혼자 string으로 변환 후 입력함 (사용자 입력값은 항상 문자열형태임)
# print("입력하신 값은 " + answer + " 입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #  [10: 10자리확보]
#                               #  [>: 오른쪽정렬]
#                               #  [ : 채울문자(빈값), 0을 넣으면 0으로 채워짐]

# # 양수일 땐 +로표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) # [+: 양수,음수 표시] << +,-표시도 10자리에 포함
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# # 숫자 3자리마다 콤마 찍기
# print("{0:,}".format(100000000000))

# # +-부호도 붙이기
# print("{0:+,}".format(100000000000))
# print("{0:-,}".format(-100000000000))

# # 3자리마다 콤마, 부호, 자릿수 확보
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(10000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# # 소수점 특정자리수까지만 표시 ( 소수점 셋째 자리에서 반올림)
# print("{0:.2f}".format(5/3))


# 파일 열고 닫기 (파일은 항상 열고 마지막에 닫아줘야함.)
# score_file = open("score.txt", "w", encoding="utf8") # w = write 쓰기용도
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a = 이미 존재하는 파일에 append(추가)
# score_file.write("과학은 : 80")
# score_file.write("\n코딩 : 100") # .write는 자동으로 줄바꿈이 되지않아서 \n을 추가함.
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r = read
# print(score_file.read()) # 파일의 모든 내용을 읽어옴
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동 end="" 줄바꿈없이 이어붙이기
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle : 데이터를 파일형태로 저장해준다. pickle.dump , pickle.load
# import pickle
# profile_file = open("profile.pickle", "wb") # wb : write, binary, 인코딩 필요없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # (중요) profile에 있는 정보를 file에 저장 
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
    # study_file.write("파이썬을 열심히 하고있어요")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())

# 마린 : 공격유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 일반유닛 (부모클래스)
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name     # 멤버변수
#         self.hp = hp         # 멤버변수
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것
# # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # wraith2.clocking = True # class 외부에서 속성을 추가할 수 있음

# # if wraith2.clocking == True:
# #     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

# # 공격 유닛 (자식클래스)
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage # 멤버변수

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # # 메딕 : 의무병

# # # 파이어뱃 : 공격유닛, 화염방사기
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # # 공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)

# # 드랍쉽 : 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송 . 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속시에는 클래스를 ,구분자를 통해 이어서 쓰면 됨
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상speed = 0
#         Flyable.__init__(self, flying_speed)
        
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# 발키리 : 공중 공격유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음 ,공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # Unit = super() , 차이점 : 파라미터의 self와 ()소괄호의 유무
#         self.location = location


        # pass # 아무것도 안하고 일단 넘어간다는 의미

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# 예외처리 ( try, except )
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0]) / nums[1])
#     print("{0} / {1} = {2}".format(nums[0], nums[1], int(nums[2])))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # as err 
#     print(err)                   # print(err) <- 그에러 명을 가져옴
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# class BigNumberError(Exception): # Exception이라는 함수를 상속받는 내가만든 Exception 클래스
#     def __init__(self, msg):
#         self.msg = msg

#     def bbbbbb(self):
#         return self.msg
    

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))    # 위의 if 조건에 걸리면 의도적으로 ValueError를 발생 시킬 수 있음. (raise 사용!)
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생 하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)
# except Exception as err:
#     print(err)
# finally: # 마지막에 무조건 출력
#     print("계산기를 이용해 주셔서 감사합니다.")

#모듈 (theater_module.py) 같은 경로내에 파일이 있어야함
# import theater_module
# theater_module.price(3) # 3명 영화보러 갔을때 가격
# theater_module.price_morning(4) # 4명 조조할인 가격
# theater_module.price_soldier(5) # 5명 군인할인 가격

# import theater_module as mv # 모듈명이 길때에는 별명을 사용해서 줄여서 사용하자
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # 위처럼 별명도 사용하기 싫을때는 함수 모두 import 해버리기
# from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 명시적으로 원하는 함수만 가져다 쓸 수 있음
# price(3)
# price_morning(4)
# price_soldier # 오류 (import 하지 않음)

# from theater_module import price_soldier as price # 함수 하나만 지정할때에는 별명 지정 가능
# price(5) # = price_soldier

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage() # 생성한 class
# trip_to.detail()

# from travel.thailand import ThailandPackage # 파일은 파일 자체 import 가능, 그러나 함수나 class는 from을 사용해야함
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# import travel.vietnam
# trip = travel.vietnam.VietnamPackage()
# trip.detail()

# __all__

# from random import *
# from travel import * 
# trip_to = vietnam.VietnamPackage() # 오류, 공개범위를 설정해줘야함.import되길 원하는것만 공개,비공개 설정가능(__init__.py)
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# from travel import *
# import inspect
# import random
# print(inspect.getfile(thailand)) # 파일 위치 찾기

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# input : 사용자 입력을 받는 함수
# language = input("무슨언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# print(dir())
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random # 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random)) # random모듈내에서 쓸수 있는것들을 보여줌\

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


# glob : 경로 내의 폴더/ 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder): # folder가 있으면 구문을 타라
#     print(" 이미 존재하는 폴더입니다. ")
#     os.rmdir(folder) # remove dir
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 시간 format 설정

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후