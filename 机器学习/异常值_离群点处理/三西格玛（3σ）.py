
'''
三西格玛（3σ）

当数据服从正态分布时，99%的数值应该位于距离均值3个标准差之内的距离，P(|x−μ|>3σ)≤0.003，当数值超出这个距离，可以认为它是异常值。

正态分布状况下，数值分布表：
数值分布
在数据中的占比

(μ-σ,μ+σ)
0.6827

(μ-2σ,μ+2σ)
0.9545

(μ-3σ,μ+3σ)
0.9973

注：在正态分布中σ代表标准差，μ代表均值，x=μ为图形的对称轴
'''


# -*- coding: utf-8 -*-

import pandas as pd

import numpy as np

data = [2.78, 1.79, 4.73, 3.81, 2.78, 1.80, 4.81, 2.79, 1.78, 3.32, 10.8, 100.0]

# 定义3σ法则识别异常值函数

def three_sigma(data_series):

    rule = (data_series.mean() - 3 * data_series.std() > data_series) | (data_series.mean() + 3 * data_series.std() < data_series)

    index = np.arange(data_series.shape[0])[rule]

    outliers = data_series.iloc[index]

    return outliers.tolist()

data_series = pd.Series(data)

outliers = three_sigma(data_series)

print('异常值共有：{0}个，分别是：{1}'.format(len(outliers), outliers))

# 输出：异常值共有：1个，分别是：[100.0]




