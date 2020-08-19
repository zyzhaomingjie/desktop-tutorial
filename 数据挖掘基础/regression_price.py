import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import datasets
from sklearn import linear_model

x_df=pd.DataFrame(datasets.load_boston()['data'],columns=datasets.load_boston()['feature_names']) #X
y_df=pd.DataFrame(datasets.load_boston()['target'],columns=['y']) #Y
df=x_df.join(y_df)

x = np.array(x_df)
y = np.array(y_df)


#RM与y的散点图,大致具备线性关系
plt.scatter(x[:,5], y) 
plt.show
#DIS与y的散点图,不具备线性关系
plt.scatter(x[:,7], y) 
plt.show
#PTRATIO与y的散点图,不具备线性关系
plt.scatter(x[:,10], y) 
plt.show
#c与y的散点图,大致具备线性关系
plt.scatter(x[:,12], y) 
plt.show



#尝试进行线性回归,使用RM,DIS,PTRATIO,LSTAT预测房价y,写出回归方程
x_df1 = x_df[['RM', 'DIS', 'PTRATIO', 'LSTAT']]
x1 = np.array(x_df1)
reg = linear_model.LinearRegression()
model = reg.fit(x1, y)
model.coef_##系数array([[ 4.22379223, -0.55192634, -0.97364584, -0.66543598]])
model.intercept_##截距array([24.47135762])


#解释下RM与Y的关系，他们是正相关关系
model = reg.fit(x_df[['RM']], y)
model.coef_##系数array([[9.10210898]])
model.intercept_##截距array([-34.67062078])


#对某新小区,其RM=8,DIS=2,PTRATIO=12,LSTAT=22,预测该小区房价
model.predict([[8, 2, 12, 22]])##array([[30.83450099]])


















