# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:49:34 2021

@author: vikas
"""

import pandas as pd

df = pd.read_csv('house.csv')

df.columns

x = df['area'].values
x = x[:-2]
x
x.shape

x = x.reshape(-1,1)
x.shape

x

y = df['Price'].values
y = y[:-2]

x.shape
y.shape


import matplotlib.pyplot as plt

plt.scatter(x, y)


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model
model.fit(x,y)

y_pred = model.predict(x)
y_pred
y

model.intercept_
model.coef_

r2 = model.score(x,y)
r2

plt.scatter(x,y)
plt.scatter(x, y_pred)


import numpy as np
x_test = np.array([2500, 2100, 1050]).reshape(-1,1)
x_test.shape


y_test =model.predict(x_test)
y_test


plt.scatter(x,y)
plt.scatter(x, y_pred)
plt.scatter(x_test,y_test)



#%% MUltiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

x = [[0,1], [5,1], [15,2], [25,2], [35,11], [45,15], [55,34], [60,35]]
x
y = [4,5,20,14,32,22,38,43]
y
x, y = np.array(x), np.array(y)
x #2 dim ; MLR - 2 variable, 2 dim(LxB) with 2 columns
y #1 dim
x.shape, y.shape

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x,y)

r2 = model.score(x,y)

y_pred = model.predict(x)

y_pred

y


x_test = np.array([[1,5],[10,3]])

x_test.shape

y_test = model.predict(x_test)
y_test

























