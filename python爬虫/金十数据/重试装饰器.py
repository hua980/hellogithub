'''
题目：1.请写一个含有一个重试次数默认为3的重试装饰器,如果三次失败则抛出异常
'''
# # 方法1 设置一个重试次数阈值，超出后抛出异常
# import time
# def MyRetry(func):
#     def wrapper(*args, **kwargs):
#         flage = 0 # 重试次数标志
#         max_time = 3 # 最大重试次数
#         while True:
#             if flage >= max_time:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(e)
#                 break
#             else:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     pass    #未达到重试次数最大值则跳过
#             flage += 1
#             print('第',flage,'次重试')
#             time.sleep(0.2)
#     return wrapper
#
# def function():
#     a='3'+5
#     return a
#
# funct=MyRetry(function)
# funct()

#方法2
# import requests
# from retrying import retry
#
#
# # 全部报错才会报错，如果其中一次正常，则继续执行
# # 两次retry之间等待2秒，重试3次
#
# @retry(stop_max_attempt_number=3, wait_fixed=1000)
# def _get_request(url):
#     response = requests.get(url, headers=headers, timeout=1)
#     return response.content.decode()
#
#
# def get_request(url):
#     try:
#         html_str = _get_request(url)
#     except Exception as e:
#         # print(e)
#         html_str=e
#     return html_str
#
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
# url = "https://www.baidu.com/"
# print(get_request(url))


# 方法二.直接利用python中的方法：@retry()装饰器
from retrying import retry
# stop_max_attempt_number 重试次数 ；wait_fixed 两次retry之间等待时间
@retry(stop_max_attempt_number=3, wait_fixed=1000)
def get():
    a='3'+1
    return a

def get_result():
    try:
        html_str = get()
    except Exception as e:
        html_str=e   #若三次重试失败，抛出异常
    return html_str

print(get_result())

