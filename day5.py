# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:34:21 2021

@author: vikas
"""

import pandas as pd
pd.__version__


import pydataset

from pydataset import data

data('')

mt = data('mtcars')

type(mt)
mt

mt.to_csv('D:\\ML-Lab\\mtcars.csv')

mt.head()

mt.head(10)

mt.tail(2)


import pandas as pd
adv = pd.read_csv('D:\\ML-Lab\\Dataset\\advertising.csv')
adv
type(adv)


ps1 = pd.Series([1,2,3,4,5])

ps1

type(ps1)

ps1.values

ps1.index


a1 = adv.iloc[0:10]

a2 = adv.iloc[30:40]

a1
a2

a3 = pd.concat([a1,a2])

a3

a3.shape[0]

ps2 = pd.Series(range(0,a3.shape[0]))

ps2

a4 = a3.set_index(ps2)
a4

a4.index

type(a4.values)

ps3 = pd.Series([1,22,34,56,66])
ps3


ps3 = pd.Series([1,22,34,56,66], index=['a','b','c','d','e'])
ps3

ps3['a']
ps3['a':'c']


ps3 = pd.Series([1,22,34,56,66], index=['a','b','b','d','e'])
ps3

ps3['b']


ps3.loc['b']

ps3.iloc[1]


import numpy as np
ps4 = pd.Series(np.random.randint(100, 200, size=10))

ps4

ps4>150

ps4[ps4>150]

ps4
ps4[(ps4>150) & (ps4<180)]



pd5 = pd.Series(['a','b','c'])
pd5


import pandas as pd
course = pd.Series(['BTech', 'MTech', 'MBA', 'BBA'])
course
strength = pd.Series([100, 50, 120, 90])
strength
fees = pd.Series([10, 20, 12, 22])
fees

d1 = {'Course':course, 'Strength':strength, 'Fees':fees}

d1
df1 = pd.DataFrame(d1)

df1

df1.iloc[0:2]

df1.loc[0:2]

df1['Course']

df1[['Course','Strength']]


df1
df1.count()

adv.columns

df1.describe()

df1.dtypes


df1

df1[df1['Course']=='BBA']


import pandas as pd
course = pd.Series(['BTech', 'MTech', 'MBA', 'BBA', 'BBA'])
course
strength = pd.Series([100, 50, 120, 90, 50])
strength
fees = pd.Series([10, 20, 12, 22, 13])
fees

d1 = {'Course':course, 'Strength':strength, 'Fees':fees}

d1
df1 = pd.DataFrame(d1)

df1[(df1['Course']=='BBA') & (df1['Fees']==22)]

df1

df1[df1['Strength']>=100]

df1

df1.drop(4)

df2 = df1.drop('Fees', axis=1 )

df2


df1
df1[df1['Course']=='BBA']
df1[df1['Course']=='BBA'].index
df1.drop(df1[df1['Course']=='BBA'].index)


df1
df1.sum()
df1.max()
df1.min()
df1.std()
df1.mean()
df1.median()
df1.dtypes

df1
placed = pd.Series([None,np.nan, 100, None, np.nan])

df1['Placed'] = placed

df1

df1.isnull()
df1.notnull()

df1
df1.describe()

df1.dropna(axis=0)
df1.dropna(axis=1)



adv = pd.read_csv('advertising.csv')
adv



adv.describe()
n1 = adv.isnull().values
type(n1)
sum(n1)



adv = adv.dropna()
adv.describe()
n1 = adv.isnull().values
type(n1)
sum(n1)


adv.dtypes

for i in adv.columns:
    print(adv[adv[i].isnull()].index.tolist())

adv.dropna(axis='rows')

adv.dropna(axis='columns')

adv.dropna(axis='columns', how= 'all')

adv.dropna(axis='columns', how= 'any')


'''
pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000, None], [None, None, None, None, None], ['kanika', 28, None, 5000, None], ['tanvi', 20, 'F', None, None], ['poonam',45,'F',None,None],['upen',None,'M',None, None]])
pd4
pd4.dropna(axis=1,thresh=1)
'''

import numpy as np
ps4 = [None, np.nan, None, np.nan, np.nan , None]

pd4
pd4['nan'] = ps4
pd4
pd4.shape[0]

pd4

pd4.fillna(0)


import pandas as pd

df1 = pd.read_csv('airline.csv')

df1

df1.plot()

df1.fillna(0).plot()

df2 = df1.fillna(method='ffill')
df2.plot()


df2.dtypes
df2.columns
df2['passengers'].plot()


ps4 = pd.Series([None, None,200, None, 400, None, None, 700])

ps4
ps4 = ps4.fillna(method='ffill')

ps4
ps4.fillna(method='bfill')



grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }
df1 = pd.DataFrame(grades1)
df1
grades2 = {'subject3': ['A1','B1','A2','A3'],'subject4': ['A2','A1','B2','B3']}

df2 = pd.DataFrame(grades2)
df2
pd.concat([df1,df2], axis=1)
































