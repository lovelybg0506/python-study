
'''

@echo off
mkdir "C:\IE"
echo CreateObject("InternetExplorer.Application").Visible=true> "C:\IE\InternetExplorer.VBS"

메모장에 이렇게 쓰고.bat 확장자파일로 저장하면됨
'''

'''
설명

@echo off       : on쓰면  아래에 쓴 명령어가 cmd에 보임, off쓰면 안보임
mkdir "C:\IE"   : 경로에 폴더생성해줘
echo ~ >        : echo 다음에 적은 문자 써서 >꺽쇠다음에 써진 경로에다가 파일만들어줘

'''

