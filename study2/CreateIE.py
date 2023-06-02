
# pip install pyinstaller
# pyinstaller --onefile CreateIE.py   

import os

memo = 'CreateObject("InternetExplorer.Application").Visible=true'

# 파일 경로와 이름
file_path = r"C:\IE\InternetExplorer.VBS"

# 폴더생성
folder_path = os.path.dirname(file_path)
os.makedirs(folder_path, exist_ok=True)

# 파일 생성 및 쓰기
with open(file_path, "w") as file:
    file.write(memo)

print("파일이 생성되었습니다.")
