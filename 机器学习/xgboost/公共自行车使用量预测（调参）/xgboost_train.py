
#参考：https://www.cnblogs.com/wj-1314/p/10620131.html

#_*_coding:utf-8_*_
import numpy as np
import pandas as pd


def load_data(trainfile, testfile):
    traindata = pd.read_csv(trainfile)
    testdata = pd.read_csv(testfile)
    # print(traindata.shape)   #(10000, 9)
    # print(testdata.shape)    #(7000, 8)
    # print(traindata)
    # print(type(traindata))
    feature_data = traindata.iloc[:, 1:-1]
    label_data = traindata.iloc[:, -1]
    test_feature = testdata.iloc[:, 1:]
    return feature_data, label_data, test_feature

# -----------网格搜索调参----------
#n_estimators（树的个数） 参数选取
def xgboost_parameter_tuning1(feature_data, label_data, test_feature, submitfile):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import GridSearchCV

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)

    param_test1 = {
        'n_estimators': range(100, 1000, 100)
    }
    gsearch1 = GridSearchCV(estimator= xgb.XGBRegressor(
        learning_rate=0.1, max_depth=5,
        min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8,
        nthread=4, scale_pos_weight=1, seed=27),
        param_grid=param_test1, cv=5
    )


    gsearch1.fit(X_train, y_train)
    return gsearch1.best_params_, gsearch1.best_score_

#调参 max_depth(树的最大深度)和min_child_weight(孩子节点中的最小的样本权重和)
def xgboost_parameter_tuning2(feature_data, label_data):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import GridSearchCV

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)

    param_test2 = {
        'max_depth': range(3, 10, 1),
        'min_child_weight': range(1, 6, 1),
    }
    gsearch1 = GridSearchCV(estimator= xgb.XGBRegressor(
        learning_rate=0.1, n_estimators=200
    ), param_grid=param_test2, cv=5)


    gsearch1.fit(X_train, y_train)
    return gsearch1.best_params_, gsearch1.best_score_

# gamma(用于控制是否后剪枝的参数，越大越保守)参数调优
def xgboost_parameter_tuning3(feature_data, label_data):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import GridSearchCV

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)

    param_test3 = {
        'gamma': [i/10.0 for i in range(0, 5)]
    }
    gsearch1 = GridSearchCV(estimator=xgb.XGBRegressor(
        learning_rate=0.1, n_estimators=200, max_depth=5, min_child_weight=5
    ), param_grid=param_test3, cv=5)


    gsearch1.fit(X_train, y_train)
    return gsearch1.best_params_, gsearch1.best_score_

# 调整subsample(随机采样训练样本) 和 colsample_bytree(这个参数默认为1，是每个叶子里面h的和至少是多少) 参数
def xgboost_parameter_tuning4(feature_data, label_data):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import GridSearchCV

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)

    param_test4 = {
        'subsample': [i / 10.0 for i in range(6, 10)],
        'colsample_bytree': [i / 10.0 for i in range(6, 10)]
    }
    gsearch1 = GridSearchCV(estimator=xgb.XGBRegressor(
        learning_rate=0.1, n_estimators=200, max_depth=5, min_child_weight=5,gamma=0.0
    ), param_grid=param_test4, cv=5)


    gsearch1.fit(X_train, y_train)
    return gsearch1.best_params_, gsearch1.best_score_

# 正则化参数调优
def xgboost_parameter_tuning5(feature_data, label_data):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import GridSearchCV

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)

    param_test5 = {
        'reg_alpha': [0, 0.001, 0.005, 0.01, 0.05]
    }
    gsearch1 = GridSearchCV(estimator=xgb.XGBRegressor(
        learning_rate=0.1, n_estimators=200, max_depth=5, min_child_weight=5, gamma=0.0,
        colsample_bytree=0.9, subsample=0.8), param_grid=param_test5, cv=5)

    gsearch1.fit(X_train, y_train)
    return gsearch1.best_params_, gsearch1.best_score_

#模型的训练
def xgboost_train(feature_data, label_data, test_feature, submitfile):
    import xgboost as xgb
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

    X_train, X_test, y_train, y_test = train_test_split(feature_data, label_data, test_size=0.23)
    params = {
        'learning_rate': 0.1,
        'n_estimators': 200,
        'max_depth': 5,
        'min_child_weight': 5,
        'gamma': 0.0,
        'colsample_bytree': 0.9,
        'subsample': 0.7,
        'reg_alpha': 0.001,

    }
    model = xgb.XGBRegressor()
    # model.fit(X_train, y_train)
    model.fit(feature_data, label_data)
    # 对测试集进行预测
    y_pred = model.predict(X_test)
    # 计算准确率
    MSE = mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    print('均方根误差（RMSE）:', RMSE)

    print("随机森林回归的默认评估值为：", model.score(X_test, y_test))
    print("随机森林回归的R_squared值为：", r2_score(y_test, y_pred))
    print("随机森林回归的均方误差为:", mean_squared_error(y_test, y_pred))
    print("随机森林回归的平均绝对误差为:", mean_absolute_error(y_test, y_pred))

    submit = pd.read_csv(submitfile)
    submit['y'] = model.predict(test_feature)
    # submit.to_csv('my_xgboost_prediction1.csv', index=False)


if __name__ == '__main__':
    trainfile = 'data/train.csv'
    testfile = 'data/test.csv'
    submitfile = 'data/sample_submit.csv'
    feature_data, label_data, test_feature = load_data(trainfile, testfile)

    # 调参
    best_params1,best_score1=xgboost_parameter_tuning1(feature_data, label_data, test_feature, submitfile)
    best_params2,best_score2= xgboost_parameter_tuning2(feature_data, label_data)
    best_params3,best_score3 = xgboost_parameter_tuning3(feature_data, label_data)
    best_params4,best_score4= xgboost_parameter_tuning4(feature_data, label_data)
    best_params5, best_score5 = xgboost_parameter_tuning5(feature_data, label_data)
    print(best_params1)
    print(best_params2)
    print(best_params3)
    print(best_params4)
    print(best_params5)

    xgboost_train(feature_data, label_data, test_feature, submitfile)
