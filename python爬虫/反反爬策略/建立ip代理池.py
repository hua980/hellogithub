import requests
import parsel
import time

#检测ip的方法
def check_ip(proxies_list):
    """检测ip的方法"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

    can_use = []
    for proxy in proxies_list:
        # print(proxy)
        try:
            response = requests.get('http://www.baidu.com', headers=headers, proxies=proxy, timeout=0.1)  # 超时报错
            if response.status_code == 200:
                can_use.append(proxy)
        except Exception as error:
            print(error)
    return can_use


#爬取快代理网站的ip数据
def getip(url):
    # 1、确定爬取的url路径，headers参数
    base_url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

    # 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
    response = requests.get(base_url, headers=headers)
    data = response.text
    # print(data)

    # 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
    # 3、1 转换python可交互的数据类型
    html_data = parsel.Selector(data)
    # 3、2 解析数据
    parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr') # 返回Selector对象
    # print(parse_list)

    # 免费 IP  {"协议":"IP:port"}
    # 循环遍历，二次提取
    # proxies_list = []
    for tr in parse_list:
        proxies_dict = {}
        http_type = tr.xpath('./td[4]/text()').extract_first()
        ip_num = tr.xpath('./td[1]/text()').extract_first()
        port_num = tr.xpath('./td[2]/text()').extract_first()
        # print(http_type, ip_num, port_num)

        # 构建代理ip字典
        proxies_dict[http_type] = ip_num + ':' + port_num
        # print(proxies_dict)
        proxies_list.append(proxies_dict)

    # print(proxies_list)
    # print("获取到的代理ip数量：", len(proxies_list), '个')
    # return proxies_list

def nextPage(url_model):
    # 获取前10页的代理ip
    for i in range(1, 10):
        url = url_model.format(i)
        getip(url)
        time.sleep(1)
        print(url)


if __name__ == '__main__':
    proxies_list = []
    # 快代理
    url_model_list = ["https://www.kuaidaili.com/free/inha/{}",  # 国内高匿代理
                      "https://www.kuaidaili.com/free/intr/{}"  # 国内普通代理
                      ]
    nextPage(url_model_list[0])
    nextPage(url_model_list[1])
    # 检测代理ip可用性
    can_use = check_ip(proxies_list)

    print("获取到的代理ip数量：", len(proxies_list), '个')
    # print("能用的代理：", can_use)
    print("能用的代理数量：", len(can_use))