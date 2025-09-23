import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

#读取数据
dataset = pd.read_csv("breast_cacer_data.csv")
#print(dataset)

#提取特征 x

X = dataset.iloc[:,: -1]
#print(X)

#Y = dataset.iloc[-1]
Y = dataset['target']
#print(Y)

#划分数据集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

#数据归一化
sc = MinMaxScaler(feature_range=(0,1))

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
#print(x_train)
#print(x_test)

#逻辑回归模型搭建
lr = LogisticRegression()
lr.fit(x_train, y_train)

#打印模型参数
print('W:', lr.coef_)
print('b', lr.intercept_)


#利用训练号的模型进行推理测试
pre_result = lr.predict(x_test)
print(pre_result)

#打印预测结果概率
pre_result_proba = lr.predict_proba(x_test)
print(pre_result_proba)

#获取恶性的概率
pre_list = pre_result_proba[:, 1]
print(pre_list)

#设置阈值
thresholds = 0.3

#设置保存结果的列表
result = []
result_name = []

for i in range(len(pre_list)):
    if pre_list[i] > thresholds:
        result.append(1)
        result_name.append('恶性')
    else:
        result.append(0)
        result_name.append('良性')

#打印阈值调整后的结果
print(result)
print(result_name)

#输出结果的精确度和召回率
report = classification_report(y_test, result, labels = [0, 1], target_names=['良性', '恶性'])
print(report)
