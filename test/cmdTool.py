import os
import sys


def excute_code(code):
    # 입력받은 문자 커맨드 실행후 결과 리턴
    return os.popen(code).read()

def main():
    #유저로부터 입력받음
    input1 = input()

    if input1 == '\q':
        os.system('exit')
    if input1 == '\c':
        os.system('cls')
    else:
        print(str(excute_code(input1)))
        main()

if __name__ == "__main__":
    main()
