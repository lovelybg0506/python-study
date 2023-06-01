# 네이버 Papago 언어감지 API
import os
import sys
import urllib.request
import json


def LangSensing(content):
    client_id = "MEVHPNK5arhAalSzea6V"
    client_secret = "WtZKxbUA3l"
    encQuery = urllib.parse.quote(content)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body)
        # print(response_body.decode('utf-8'))
        langCode = result['langCode']
        return langCode
    else:
        print("Error Code:" + rescode)