

# -*- coding:utf-8 -*-

from numpy import *

#创建测试数据
def loadData():
    # return [['豆奶','莴苣'],
    #  ['莴苣','尿布','葡萄酒','甜菜'],
    #  ['豆奶','尿布','葡萄酒','橙汁'],
    #  ['莴苣','豆奶','尿布','葡萄酒'],
    #  ['莴苣','豆奶','尿布','橙汁']]
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

#创建大小为1的所有数据集的集合，即将所有的单项放在一个list中
def createC1(dataSet):
    C1 = []
    for data in dataSet:
        for i in data:
            if [i] not in C1:
                C1.append([i])
    return list(map(frozenset,C1))

# 计算单元素支持度，即看数据中包含此元素的数据占总数据的比例
def degreeSupport(dataSet,C1,minSupport=0.5):
    degreeSupportList = {}  #返回支持度字典
    dataList = [] #返回满足最小支持度的元素列表
    itemCount = {}   #C1中元素在dataSet中出现的次数
    for data in dataSet:
        for item in C1:
            if item.issubset(data):  #判断item是否包含在data中
                if not item in itemCount:
                    itemCount[item] = 0
                itemCount[item] += 1
    n = float(len(dataSet))
    for key in itemCount.keys():
        support = itemCount[key]/n   #计算支持度
        if support >= minSupport:
            dataList.append(key)
        degreeSupportList[key] = support
    return dataList,degreeSupportList

# 数据合并
# 如果数据长度为n，取前n-1个元素相同的两个数据合并组成新的数据，这样不必计算所有的组合，可以省略剪枝步骤
def merge(L,k):
    n = len(L)
    dataMergeList = []
    for i in range(n-1):
        for j in range(i+1,n):
            L1 = list(L[i])[:k]
            L2 = list(L[j])[:k]
            L1.sort()
            L2.sort()
            if L1 == L2:
                dataMergeList.append(L[i] | L[j])
    return dataMergeList

#
def apriori(dataSet,minSupport=0.5):
    dataSet = list(map(set,dataSet))    #数据集合中的数据去重[[1,1,2]] --> [[1,2]]
    C1 = createC1(dataSet)
    L1, degreeSupportList = degreeSupport(dataSet, C1, minSupport)
    L = [L1]
    k = 0
    while len(L[k]) > 1:  #创建包含更大项集的更大列表,直到下一个大的项集为1
        Lm = merge(L[k],k)
        Lk,support = degreeSupport(dataSet,Lm,minSupport)
        L.append(Lk)
        degreeSupportList.update(support)
        k += 1
    return L,degreeSupportList


def confCalculation(L,data,degreeSupportList,minConf,bigRulesList):
    n = len(data)
    for i in range(n-1):   #取n = len(data)的目的是取到L中数据长度为n-1即可，否则后面的长度大于或者等于data的长度，再计算没有意义了
        for d in L[i]:
            if d.issubset(data):
                conf = degreeSupportList[data]/degreeSupportList[data-d]
                if conf > minConf:
                    print(data-d,'-->',d,'conf:',conf)
                    bigRulesList.append((data-d,d,conf))

#创建关联规则
def genetateRules(L,degreeSupportList,minConf = 0.5):
    bigRulesList = []
    n = len(L)
    for i in range(1,n):
        for j in L[i]:
            confCalculation(L, j, degreeSupportList, minConf, bigRulesList)
    return bigRulesList

dataSet = loadData()
# print(dataSet)
# C1 = createC1(dataSet)
# print(C1)
# L1,degreeSupportList = degreeSupport(dataSet,C1,0.5)
# print(L1)
# print(degreeSupportList)
L,degreeSupportList = apriori(dataSet,0.5)
print('频繁项集：\n',L,'\n')
print('关联规则：\n',degreeSupportList,'\n')

print('强关联规则：',)
rulesList = genetateRules(L,degreeSupportList,0.7)
print(rulesList)

