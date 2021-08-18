

# 加载数据
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


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
distortions = []
for i in range(1, 10):
        km = KMeans(n_clusters=i,
                    init='k-means++',
                    n_init=10,
                    max_iter=300,
                    random_state=0)
        km.fit(all_points)
        distortions.append(km.inertia_)

plt.plot(range(1,10), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()
