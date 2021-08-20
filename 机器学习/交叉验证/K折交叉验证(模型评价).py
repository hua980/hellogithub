'''
使用sklearn库中的鸢尾花数据集，并针对以下模型使用cross_val_score来衡量每个模型的性能。 最后找出性能最佳的模型。
（1）逻辑回归
（2）支持向量机
（3）决策树
（4）随机森林
参考：https://blog.csdn.net/weixin_37763870/article/details/105393467?

交叉验证：
import sklearn.model_selection as ms
# 使用给出的模型,针对输入与输出进行5次交叉验证
# 把每次交叉验证得到的精准度得分以数组的方式返回
score = ms.cross_val_score(
    模型, 输入集, 输出集,
    cv=5,          	   # 交叉验证的次数
    scoring='accuracy' # 指标名称 (精准度)
)

'''

from sklearn.datasets import load_iris  #加载load_iris数据集
from sklearn.model_selection import cross_val_score  #交叉验证模块
from sklearn.linear_model import LogisticRegression  #逻辑回归
from sklearn.tree import DecisionTreeClassifier  #决策树
from sklearn.svm import SVC   #支持向量机
from sklearn.ensemble import RandomForestClassifier  #随机森林
import numpy as np   #数值运算模块

iris = load_iris()

# 1.逻辑回归
# 采用十折交叉验证，将会返回10次准确率得分，然后用np.average求平均。
lr_scores = cross_val_score(LogisticRegression(max_iter=3000),iris.data,iris.target,cv=10)
# print(lr_scores)
print('逻辑回归准确率：',np.average(lr_scores))

# 2.决策树
d_scores = cross_val_score(DecisionTreeClassifier(),iris.data,iris.target,cv=10)
# print(d_scores)
print('决策树准确率：',np.average(d_scores))

# 3.支持向量机
s_scores = cross_val_score(SVC(),iris.data,iris.target,cv=10)
# print(s_scores)
print('支持向量机准确率：',np.average(s_scores))


# 4.随机森林
rf_scores = cross_val_score(RandomForestClassifier(n_estimators=40),iris.data,iris.target,cv=10)
# print(rf_scores)
print('随机森林准确率：',np.average(rf_scores))