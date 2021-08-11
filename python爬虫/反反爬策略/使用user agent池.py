

# User-Agent池：
# 反爬更好的方式是使用User-Agent池来解决(如随机生成User-Agent）
#方法1
import random
import requests

def get_ua():
    first_num = random.randint(55, 76)
    third_num = random.randint(0, 3800)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_14_5)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    headers = {
        'User-Agent': ua
    }
    return headers
headers=get_ua()
print(headers)


#方法2
from fake_useragent import UserAgent

# 实例化 user-agent 对象
ua = UserAgent(verify_ssl=False)
print(ua.random)
print(ua.random)
print(ua.random)


#方法3
#实现一个随机生成 user-agent的类
class tencent_movie(object):
    def __init__(self):
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 100):
            self.headers = {
                'User-Agent': ua.random       #随机生成user-agent
            }
    def get_html(self,url):
        response=requests.get(url,headers=self.headers)
        html=response.content.decode('utf-8')
        return html


re=tencent_movie()
print(re.headers)