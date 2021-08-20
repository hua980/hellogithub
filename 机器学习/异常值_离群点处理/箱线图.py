'''
箱线图（box plot）

    和3σ原则相比，箱线图依据实际数据绘制，真实、直观地表现出了数据分布的本来面貌，且没有对数据作任何限制性要求（3σ原则要求数据服从正态分布或近似服从正态分布）。

    其判断异常值的标准以四分位数和四分位距为基础。四分位数给出了数据分布的中心、散布和形状的某种指示，具有一定的鲁棒性，
    即25%的数据可以变得任意远而不会很大地扰动四分位数，所以异常值通常不能对这个标准施加影响。鉴于此，箱线图识别异常值的结果比较客观，因此在识别异常值方面具有一定的优越性。
'''

# -*- coding: utf-8 -*-

import pandas as pd

data = [2.78, 1.79, 4.73, 3.81, 2.78, 1.80, 4.81, 2.79, 1.78, 3.32, 10.8, 100.0]

# 定义箱线图识别异常值函数

def box_plot(data_series):

    q_abnormal_low = data_series.quantile(0.25) - 1.5 * (data_series.quantile(0.75) - data_series.quantile(0.25))

    q_abnormal_up = data_series.quantile(0.75) + 1.5 * (data_series.quantile(0.75) - data_series.quantile(0.25))

    index = (data_series < q_abnormal_low) | (data_series > q_abnormal_up)

    outliers = data_series.loc[index]

    return outliers.tolist()

sorted_data = sorted(data)

data_series = pd.Series(sorted_data)

outliers = box_plot(data_series)

print('异常值共有：{0}个，分别是：{1}'.format(len(outliers), outliers))