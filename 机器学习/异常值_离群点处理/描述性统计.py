'''
1. 描述性统计

基于常识或经验，假定我们认为大于10的数值是不符合常理的。

下面用Python代码实现用描述性统计求异常值：
      df.describe() 简单观察数据特征
'''

# -*- coding: utf-8 -*-

data = [2.78, 1.79, 4.73, 3.81, 2.78, 1.80, 4.81, 2.79, 1.78, 3.32, 10.8, 100.0]

threshold = 10

# 定义描述性统计识别异常值函数

def descriptive_statistics(data):
    return list(filter(lambda x: x > threshold, data))

outliers = descriptive_statistics(data)

print('异常值共有：{0}个，分别是：{1}'.format(len(outliers), outliers))

# 输出：异常值共有：2个，分别是：[10.8, 100.0]