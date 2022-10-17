#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 6:00 下午
# @Author  : LiangJun
# @Filename    : automatic.py

import requests

# python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = str(round(time.time() * 1000))
secret = '加签时生成的密钥'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)

url = "https://oapi.dingtalk.com/robot/send?access_token=996ff636ef63ffc027d3c73091bc58fdeb4f486d413ee8af4d0938265345d270"

print(url)
headers = {
    'Content-Type': 'application/json'
}
json = {"msgtype": "markdown",
        "markdown": {
            "title": "ttt",
            "text": "取餐了@所有人"
        }}
resp = requests.post(url, headers=headers, json=json)
print(resp.text)