
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


# Calinski-Harabasz分数值ss越大则聚类效果越好
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
ch_scores = []
for i in range(2, 10):
    km = KMeans(        n_clusters=i,
                        init='k-means++',
                        n_init=10,
                        max_iter=300,
                        random_state=0      )
    km.fit(all_points)
    ch_scores.append(metrics.calinski_harabasz_score(all_points, km.labels_))
plt.plot(range(2,10), ch_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('calinski_harabaz_score')
plt.show()
