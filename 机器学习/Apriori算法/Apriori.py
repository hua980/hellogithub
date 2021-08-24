
# -*- coding: utf-8 -*-
""""
     author = "Cpz"
     time = "2019-7-22"
     aim = "Python实现Apriori关联算法"

     为了程序方便我们将
     牛奶：1
     水果：2
     尿不湿：3
     钢笔：4
     啤酒：5
"""""

import numpy as np
from itertools import combinations  # 迭代工具


data = [['牛奶' ,'水果' ,'啤酒'], ['水果' ,'钢笔'], ['水果' ,'尿不湿'], ['牛奶' ,'水果' ,'钢笔'], ['牛奶' ,'尿不湿'], ['水果' ,'尿不湿'], ['牛奶' ,'尿不湿'], ['牛奶' ,'水果' ,'尿不湿' ,'啤酒'], ['牛奶' ,'水果' ,'尿不湿']]
minsp = 2

data1 = [[1 ,2 ,5], [2 ,4], [2 ,3], [1 ,2 ,4], [1 ,3], [2 ,3], [1 ,3], [1 ,2 ,3 ,5], [1 ,2 ,3]]

d = []
for i in range(len(data)):
    d.extend(data1[i]  )  # 样本集化为一维数组
new_d = list(set(d))
# 去重




C = np.zeros([len(new_d), 2]  )  # 创建指定大小的数组，数组元素以 0 来填充,2列：


def limit(L):  # 删掉不满足阈值的C
    row = []
    for i in range(L.shape[0]):
        # print(L[i:-1])
        if L[i, -1] < minsp:
            row.append(i)
    L = np.delete(L, row, 0)

    return L

def satisfy(s ,s_new ,k):  # 更新，删除不满足支持度的L
    e = []
    ss_new = []
    for i in range(len(s_new)):
        # print(s_new[i])
        for j in combinations(s_new[i], k):  # 迭代每个频繁集可能出现的元素组合
            e.append(list(j))
        if ([l for l in e if l not in s]) == []:
            ss_new.append(s_new[i])
        e = []
    # print(ss_new)
    return ss_new



def count(s_new):
    num = 0
    # print(s_new)
    C = np.copy(s_new)  # 转化成narray表示的函数
    C = np.column_stack((C ,np.zeros(C.shape[0])))  # 对C（k+1）生成的数组 添加计数列
    # print(C)
    for i in range(len(s_new)):  # 项集Ck到data数据集计出现频率
        for j in range(len(data1)):
            if ([l for l in s_new[i] if l not in data1[j]]) == []:
                num = num + 1
        C[i ,-1] = num
        num = 0
    # print(C)
    return C






def generate(L ,k):  # 实现由L向C的转换
    s = []
    for i in range(L.shape[0]):
        s.append(list(L[i ,:-1]))  # 把商品值添加到数组s中

    s_new = []
    for i in range(L.shape[0 ] -1):
        for j in range( i +1 ,L.shape[0]):  # 二重循环生成Ck项集
            # print(L[j,-2],L[i,-2])
            if(L[j ,-2 ] >L[i ,-2]):
                t = list(np.copy(s[i]))
                # print(t)
                t.append(L[j ,-2])
                # print(t)
                s_new.append(t)

    s_new = satisfy(s ,s_new ,k)

    C = count(s_new)
    return C

# 对C1项集进行支持度计数
for i in range(len(new_d)):
    C[i:] = np.array([new_d[i], d.count(new_d[i])])

# 将C1项集复制给频繁集L1
L = np.copy(C)
L = limit(L)
# print(L)

# # 开始迭代
k = 1
while (np.max(L[: ,-1]) > minsp):
    C = generate(L, k)  # 由L产生C
    L = limit(C)        # 由C产生L
    k = k+ 1

print(list(set(tuple(t) for t in L)))  # 对结果去重

'''
    最终我们得到两个满足支持度的关联规则，从这五条购物清单知道
    用户会购买
    1.牛奶和水果的同时会有可能买尿不湿
    2.牛奶和水果的同时会有可能买啤酒
    所以一个简单的预测功能就出现了：
    可以去找买牛奶的用户向他们推荐水果和尿不湿或者啤酒
'''