# Client ID : TVq2GqB8fYAfOLKVkjc_
# Client Secret : iCQCSnvLbH

import os
import sys
import urllib.request
client_id = "TVq2GqB8fYAfOLKVkjc_" # 개발자센터에서 발급받은 Client ID 값
client_secret = "iCQCSnvLbH" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

import json

if(rescode==200):
    response_body = response.read()
    TNSRATSTR = json.loads(response_body)
    b = TNSRATSTR['message']['result']['translatedText']
    print(f"A:{TNSRATSTR}")
    print(b)
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)