
# 轮廓系数 考虑了族内族外量方面的因素，系数越大越好

import numpy
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


from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
scores = []
for i in range(2, 15):
    km = KMeans(n_clusters=i,
                init='k-means++',
                n_init=10,
                max_iter=300,
                random_state=0)
    km.fit(all_points)
    scores.append(metrics.silhouette_score(all_points, km.labels_ , metric='euclidean'))
plt.plot(range(2,15), scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('silhouette_score')
plt.show()
# print(scores)