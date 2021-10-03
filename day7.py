# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:31:12 2021

@author: vikas
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([5,15,25,35,45,55])
x.shape
x = x.reshape((-1,1))
x.shape

y = np.array([5,20,14,32,22,38])  #1 dim
y.shape

plt.scatter(x,y)


model = LinearRegression()
model.fit(x,y)

model.intercept_
model.coef_


y_pred = model.predict(x)
y_pred

plt.scatter(x,y)
plt.scatter(x, y_pred)

rs = model.score(x,y)
rs


x_pred = np.array([10, 32, 60, 67, 81]).reshape((-1,1))
x_pred.shape


y_pred1 = model.predict(x_pred)

y_pred1

plt.scatter(x,y)
plt.scatter(x, y_pred)
plt.scatter(x_pred,y_pred1)




import numpy as np
from sklearn.linear_model import LinearRegression

x = [[0,1], [5,1], [15,2], [25,2], [35,11], [45,15], [55,34], [60,35]]
x
y = [4,5,20,14,32,22,38,43]
y

x = np.array(x)
y = np.array(y)

model = LinearRegression()
model.fit(x,y)
r2 = model.score(x,y)
r2

y_pred = model.predict(x)
y_pred

x_pred = np.array([[10,5], [32,5]])
x_pred.shape


y_pred1 = model.predict(x_pred)
y_pred1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

from sklearn.linear_model import LinearRegression


mt = data('mtcars')
mt

mt.shape

df = mt[['mpg', 'hp']]

df

plt.scatter(df['mpg'], df['hp'])


x = df['mpg'].values.reshape((-1,1))
x.shape

y = df['hp'].values
y.shape


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

x_train.shape
y_train.shape
x_test.shape
y_test.shape


model = LinearRegression()

model.fit(x_train, y_train)
rs = model.score(x,y)
rs

y_pred = model.predict(x_test)
y_pred


plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test)
plt.scatter(x_test, y_pred)







from pydataset import data
mt = data('mtcars')

mt.dtypes

mt = mt[['mpg', 'wt', 'disp', 'qsec']]

mt

import seaborn as sns
pp = sns.pairplot(mt, size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))

fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('Wine Attributes Pairwise Plots', fontsize=14)



x = mt.drop('mpg', axis=1).values

y = mt['mpg'].values


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

x_train.shape
y_train.shape
x_test.shape
y_test.shape



model = LinearRegression()
model.fit(x_train,y_train)
r2 = model.score(x,y)
r2
y_pred= model.predict(x_test)
y_pred



x_pred = np.array([[6.07 , 208.8  ,  17.4],[6.25 , 372.   ,  17.98] ])

x_pred

y_pred1 = model.predict(x_pred)
y_pred1





import statsmodels.api as sm
import matplotlib.pyplot as plt
from pydataset import data

from statsmodels.formula.api import ols

mtmodel = ols("mpg ~ wt", data =mt).fit()

print(mtmodel.summary())


pred = mtmodel.predict()
pred






from pydataset import data
mt = data('mtcars')

mt.dtypes

mt = mt[['mpg', 'wt', 'hp', 'disp', 'qsec']]

import statsmodels.api as sm
import matplotlib.pyplot as plt
from pydataset import data

from statsmodels.formula.api import ols

mtmodel = ols("mpg ~ wt + hp +  qsec", data =mt).fit()

print(mtmodel.summary())


pred = mtmodel.predict()
pred



import statsmodels.api as sm
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(mtmodel, fig=fig)




import pandas as pd
import numply as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('USA_Housing.csv')

df.columns


x = df.drop('Price', axis=1)

y = df['Price']

x.shape
y.shape

df.columns
model = ols("Price ~ age + rooms + population", data = df).fit()

model.summary()


import statsmodels.api as sm
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(model, fig=fig)




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('hourly_wages.csv')

df.columns


x = df.drop('wage_per_hour', axis=1)

y = df['wage_per_hour']

x.shape
y.shape

df.columns
model = ols("wage_per_hour ~ union + education_yrs + experience_yrs + age + female + marr + south + manufacturing +construction", data = df).fit()

model.summary()


import statsmodels.api as sm
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(model, fig=fig)

model = ols("wage_per_hour ~ education_yrs + experience_yrs + manufacturing + female+ age ", data = df).fit()

model.summary()
















































































