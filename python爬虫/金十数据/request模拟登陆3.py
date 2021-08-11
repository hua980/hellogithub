
# import requests
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
#     'accept-encoding': 'gzip, deflate, br',
#     'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1628694680; UM_distinctid=17b35c491bc17-053af7938f8253-f7f1939-144000-17b35c491bd50b; __gads=ID=1ddf012076c703a8-22e673b3c4ca0035:T=1628694678:RT=1628694678:S=ALNI_MZY_9e9WU_Wqp4cUeR8AF6Bix60lg; login_redirect=; CALENDAR_FAVOR_INDEX_LIST=%5B%5D; XSRF-TOKEN=eyJpdiI6InU3UEhmYlR5M29LRWxlUkx1UkhZNEE9PSIsInZhbHVlIjoiQm1PSGZCenpnOGFtREg3V3llYWtFdz09IiwibWFjIjoiZWVhMzNmNmM5M2M0Mzk4ZGEwM2UwNmQ0MmVjNWYyODQ2NThhNjNiOTk3NTBiNTFkMGFjMTRjNjNhNDgzNTg4NSJ9; laravel_session=eyJpdiI6IlJGQXphS3dSRVZ3OTMwREpkaGF5Mnc9PSIsInZhbHVlIjoiU1ZKdHN0Q1I5NXYyazhHWWdPdElZMlc2clNGQ0lnRFBGckJ4cis4ZzRcL3RDOTlwM1dFdGF4MlA2ZFNDMThpamtBZnpRdVBCRWdacG80XC9zTXkxSGJQQT09IiwibWFjIjoiNjg4Yjk2MWI0NzFiNzA5ZmU4NGE0YTAyMjVkNzA5NDMwNzZhMjNjYTM0MmQ4ZjFkMjc1ZWNkZGJlNDcxODU4YyJ9; x-token=; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1628695570'
# }
# session = requests.Session()
# source = session.post(url='https://uc-api.jin10.com/login_w', headers=headers)
# print(f"statusCode = {source.status_code}")
# source.encoding='utf-8'
# print(source.text)

import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#登录后才能访问的网页
url = 'https://uc-api.jin10.com/login_w'
#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str='Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1628694680; UM_distinctid=17b35c491bc17-053af7938f8253-f7f1939-144000-17b35c491bd50b; __gads=ID=1ddf012076c703a8-22e673b3c4ca0035:T=1628694678:RT=1628694678:S=ALNI_MZY_9e9WU_Wqp4cUeR8AF6Bix60lg; login_redirect=; CALENDAR_FAVOR_INDEX_LIST=%5B%5D; oauthBackUrl=https%3A%2F%2Fucenter.jin10.com%2F; XSRF-TOKEN=eyJpdiI6IjRLekx5Smt1VzM2RXh4QzBKZnpIWXc9PSIsInZhbHVlIjoieGk4SGMrT3lQTklUXC82WHlpOFhRTlE9PSIsIm1hYyI6IjA4NjNlOTk0MmU3MWE2NzY2MGZhZjliNWJkYzFmOGJkODY2MTMxOTYxZmQ5YjZkODJkYjZiYWU5OWI5YzVjMDQifQ%3D%3D; laravel_session=eyJpdiI6IkVqaFZoVmxab1pINmVOcXlSSkp0MXc9PSIsInZhbHVlIjoicmVQYndITmdmWU5SZjJYWmxkdVBlK0FsT3dJNXUyaHh2K01NblZiVVRqazJlazd4RFwvSGFrU0l4RlAwZndHenZsemo4czd5cWdcL0RlTHl3VDZ6bXQwZz09IiwibWFjIjoiNmZjOWQ0MDJiZTkyNGRkNTBhZDU4NzEzM2MwNzI4Y2M4MDM0YzMxODQ1ZjUyOTE5ZWRjMDM0OTAzNjEwNzY1YyJ9; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1628701781; x-token='
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
#设置请求头
headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
#在发送get请求时带上请求头和cookies
resp = requests.post(url, headers = headers, cookies = cookies)
print(f"statusCode = {resp.status_code}")
print(resp.content.decode('utf-8'))