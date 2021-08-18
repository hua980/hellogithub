import random

import numpy
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

all_points = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']

# 加载数据
def loadDataSet(fileName):
    dataSet = []
    fileIn = open(fileName)
    for line in fileIn.readlines():
        lineArr = line.strip().split()   #str.split()  清除默认 空格和tab  对空格数量不敏感
        dataSet.append('%0.6f' % float(lineArr[0]))
        dataSet.append('%0.6f' % float(lineArr[1]))
    dataSet = numpy.array(dataSet,dtype=float).reshape(80,2)
    return  dataSet

all_points=loadDataSet("data.txt")

# # 调用KMeans方法, 聚类数为4个，fit()之后开始聚类
kmeans = KMeans(n_clusters=4).fit(all_points)
# 调用DBSCAN方法, eps为最小距离，min_samples 为一个簇中最少的个数，fit()之后开始聚类
dbscan = DBSCAN(eps=0.132, min_samples=2).fit(all_points)

# 开始画图
plt.subplot(1, 2, 1)
plt.title('kmeans')
for i, l in enumerate(kmeans.labels_):
    plt.plot(all_points[i][0], all_points[i][1], color=colors[l], marker=markers[l])

plt.subplot(1, 2, 2)
plt.title('dbscan')
for i, l in enumerate(dbscan.labels_):
    # if l == -1
    plt.plot(all_points[i][0], all_points[i][1], color=colors[l], marker=markers[l])

plt.show()
