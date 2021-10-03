# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:05:19 2021

@author: vikas
"""

import pandas as pd

df = pd.read_csv('hourly_wages.csv')

df.dtypes

x= df.drop('wage_per_hour', axis=1).values

x

y = df['wage_per_hour'].values


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.1)

x_train.shape, x_test.shape, y_train.shape, y_test.shape


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

r2 = model.score(x,y)
r2

y_pred = model.predict(x_test)
y_pred
y_test







import pandas as pd

df = pd.read_csv('USA_housing.csv')

df.dtypes

x= df.drop('Price', axis=1).values

x

y = df['Price'].values


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.1)

x_train.shape, x_test.shape, y_train.shape, y_test.shape


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

r2 = model.score(x,y)
r2

y_pred = model.predict(x_test)
y_pred
y_test




df = pd.read_csv('USA_Housing1.csv')
df.columns

from statsmodels.formula.api import ols
MTmodel1 = ols("Price ~ income + age + rooms + population", data=df).fit()
#MTmodel1 = ols("Price ~ rooms", data=df).fit()
print(MTmodel1.summary())


fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(MTmodel1, fig=fig)














