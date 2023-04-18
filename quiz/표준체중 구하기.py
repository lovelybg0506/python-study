'''
퀴즈) 표준체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

standardWeight = 0

def std_weight(height, gender):
    if str(height).isnumeric(): # 키가 숫자인지 판단 (파이썬에서는 isnumeric 함수가 String타입일때에만 사용가능함)
        if gender == "m":       # 즉, 변수를 String으로 타입변환 후 사용해야함.
            gender = "남자"
        elif gender == "w":
            gender = "여자"
        else:
            print("성별은 'm' : 남자, 'w' : 여자로 구분해주세요")
            return

        global standardWeight
        if gender == "남자":
            standardWeight = (height*0.01) * (height*0.01) * 22
        elif gender == "여자":
            standardWeight = (height*0.01) * (height*0.01) * 21
        
        standardWeight = round(standardWeight,2)
        return print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height,gender,standardWeight))
    else:
        print("키는 숫자만입력해주세요")
        return
    
std_weight(175,"m") # 잘 나옴
std_weight(172,"w") # 잘 나옴
std_weight(176,"d") # 성별 잘못입력시
std_weight("키","m") # 키 잘못입력시