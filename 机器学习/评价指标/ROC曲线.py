
# 先构建一个偏斜的数据集，这里采用sklearn中的digits手写数据集。digits里面的特征是64的像素，不同像素中存的是颜色深度，结果是0-9这10个数字。
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
X = digits.data
y = digits.target.copy()
# 为了构建偏斜数据，将y中所有等于9的数字置为“1”，将不等于9的数字置为“0”。最后看到y中等于1的有180个样本，等于0的有1617个样本。
y[digits.target == 9] = 1
y[digits.target != 9] = 0
print(np.count_nonzero(y==1))
print(np.count_nonzero(y==0))


# 划分测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=666)

log_reg = LogisticRegression(max_iter=10000) #构建逻辑回归模型
log_reg.fit(X_train,y_train) #使用训练数据集训练模型
# y_predict = log_reg.predict(X_test) #将测试数据传入训练好的模型中，让模型预测测试数据的结果
y_predict = log_reg.predict_proba(X_test)

gbm_fpr,gbm_tpr,gbm_threasholds=roc_curve(y_test,y_predict[:,1]) # 计算ROC的值,svm_threasholds为阈值
plt.title("roc_curve of  LogisticRegression")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot(gbm_fpr,gbm_tpr)
plt.show()
