
# -*- coding: utf-8 -*-

import requests

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
header = {
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

def mafengwoLogin(account, password):
    # 马蜂窝模仿 登录
    print ("开始模拟登录马蜂窝")

    postUrl = "https://uc-api.jin10.com/login_w"
    postData = {
        'country_code': "CN",
        "mobile": account,
        "password": password,

    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    mafengwoLogin("14767512912", "123456")
