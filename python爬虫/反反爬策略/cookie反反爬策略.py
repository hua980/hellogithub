
'''
自动获取
方式一：基于Session对象实现自动处理(捕获登录前的cookie)

如何获取一个session对象？：
requests.Session()
session对象的作用：该对象可以向requests一样调用get和post发起指定请求，只不过如果在使用session发起请求的过程中如果产生了cookie，则cookie会被自动存储到该session对象中，那么就意味着下次再使用session对象发起请求，则该次请求就是携带了cookie进行的请求发送

第一次使用sessino是为了将cookie捕获且存储到session对象中，第二次使用session就是发送携带了cookie的请求
'''

# import requests
# from lxml import etree
#
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
# }
#
# # 用了自动获取的cookie每次请求都是新的cookie就非常灵活了
#
# session = requests.Session() # 创建好了seion对象
# # 第一次使用session捕获且存储cookie,猜测对雪球网首页发起的请求可能会产生cookie
# main_url = 'https://xuequi.com/'
# session.get(main_url,headers=headers) # 捕获且存储cookie
#
#
# # 含有ajax数据包的url
# url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20370786&count=15&category=-1'
# page_text = session.get(url=url,headers=headers).json() # 携带捕获的cookie发送请求
# print(page_text)


'''
cookie并不一定都是主页会产生，应该多次使用session在不同的地址下捕获cookie
方式二：基于selenium去实现获取登录后产生的cookie
这里以免密登录QQ空间为例
'''
from time import sleep
from selenium import webdriver
import requests
# 自动登录
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://qzone.qq.com/')
# driver.set_window_position(20, 40)
# driver.set_window_size(1100,700)
# 表单在该框架下
driver.switch_to.frame('login_frame')
sleep(0.5)
driver.find_element_by_xpath('//*[@id="bottom_qlogin"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys('XXXX') # 你的QQ号
driver.find_element_by_xpath('//*[@id="p"]').send_keys('XXXXX')# 你的QQ密码
driver.find_element_by_xpath('//*[@id="login_button"]').click()
'''！！！！如果输入账号密码后 弹出滑动验证码则可以这样执行
方式一：input('手动验证后输入空格继续：)
方式二： 将滑块图片保存下来 交给云打码平台，算出 X Y距离后 使用selenium动作链模拟人为验证进行登录
关于验证码识别，下一期在详解
！！！'''
# 获取cookie
cookies = driver.get_cookies()
cookies_list = []
for i in cookies:
    cookies_list.append(' '+i['name']+ '='+ i['value']) # 取出键值对，键值对前面都有一个空格，除了第一个键值对前面没有空格

cookiestr = ';'.join(cookies_list)

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Cookie':cookiestr[1:] # 开头的键值对并不需要前面的空格，如果有则会报错  可以将cookie保存到本地方便下次使用，注意有效时长问题

}

url = 'https://user.qzone.qq.com/1515768305' # 你的QQ号
response = requests.get(url,headers=headers).content.decode('utf-8') #发送携带了cookie的请求
# 成功输出登录后页面
print(response)

# 一定要注意cookie字符串的格式，第一个键值对前面没有空格，后面的每一个都有空格，要不cookie是无效的