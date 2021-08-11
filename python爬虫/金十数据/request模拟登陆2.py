# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

s = requests.Session()
url_login = "https://uc-api.jin10.com/login_w"

formdata = {
    'country_code': "CN",
    "mobile": "14767512912",
    "password": "123456",
}
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/json;charset=UTF-8",
    "Referer": "referer: https://www.jin10.com/",
    "sec-ch-ua-mobile":"?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-app-id": "YDcStOzjliuTJUvh",
    "x-app-ver": "web_base_1.0.0",
    "x-version": "1.0.0",
    'User-Agent': userAgent,
    "x-xsrf-token": "eyJpdiI6InU3UEhmYlR5M29LRWxlUkx1UkhZNEE9PSIsInZhbHVlIjoiQm1PSGZCenpnOGFtREg3V3llYWtFdz09IiwibWFjIjoiZWVhMzNmNmM5M2M0Mzk4ZGEwM2UwNmQ0MmVjNWYyODQ2NThhNjNiOTk3NTBiNTFkMGFjMTRjNjNhNDgzNTg4NSJ9",
}


r = s.post(url_login, data=formdata, headers=headers)
# 无论是否登录成功，状态码一般都是 statusCode = 200
print(f"statusCode = {r.status_code}")
content = r.text
print(content)