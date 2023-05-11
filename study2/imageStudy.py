from PIL import Image # pip install Pillow
'''
img = Image.open('images/photo1.jpg') # 이미지 open
# img = Image.open('images/photo1.jpg').convert('L') # .convert('L') -> 흑백으로 바꿈
# img = img.resize((300,500)) # 튜플형식을 이용해서 크기조절
# img.thumbnail((300,500)) # 비율 유지하며 크기조절

img = img.crop((50,50, 150,150)) # 이미지 자르기 (좌표1, 좌표2)
img.save('new_photo1.jpg', quality=75) # 변형한 이미지 저장 .save(경로와 파일명) / quality= 화질설정(0~90) 기본값 75. 용량압축용도
                                       # png파일 저장시 quantize 사용

'''

# 이미지파일 대량 비율 변환
import os
path = os.getcwd() # current working directory(현재경로)
filenames = os.listdir(path + '/images') # 이경로 안에있는 모든 파일명 리스트형식에 담음

for i in filenames:
    img = Image.open(f'images/{i}')
    img.thumbnail((500,2500))
    img.save(f'new_{i}')