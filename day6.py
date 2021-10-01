# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:00:19 2021

@author: vikas
"""

import pandas as pd

grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }

grades1

df1 = pd.DataFrame(grades1)
df1

grades2 = {'subject3': ['A31','B31','A32','A33'],'subject4': ['A42','A41','B42','B43']}

df2 = pd.DataFrame(grades2)
df2


grades2 = {'subject2': ['A31','B31','A32','A33'],'subject4': ['A42','A41','B42','B43']}

df3 = pd.DataFrame(grades2)
df3


#join
pd.concat([df1,df2], axis=0)
pd.concat([df1,df3], axis=0)

df1
df2
pd.concat([df1,df2], axis=1)
pd.concat([df1,df3], axis=1)

import pandas as pd
pd.concat([df1,df2], ignore_index=True)  #index values in order


'''
df =pd.concat([df1,df2], keys=['x','y'])  #adding multiple index
df.index.levels[0]
df.index.levels[0][1]
'''


df1
df2

import pandas as pd

grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }
df1 = pd.DataFrame(grades1)

grades2 = {'subject3': ['A31','B31','A32','A33'],'subject4': ['A42','A41','B42','B43']}
df2 = pd.DataFrame(grades2)
df = pd.concat([df1, df2], axis=1)


df.iloc[:, 0:-1]

df = df.rename(columns={'subject3':'abc1', 'subject4':'ee'})
df

df[['subject1','subject4']].columns = {'abc', 'a'}
df

df = df.rename(columns={'subject1':'abc', 'subject2':'a'} )
df


import pandas as pd

rollno = pd.Series(range(1,11))

name =[]
for i in range(1,11):
    name.append("Student"+str(i))
name

name = ["Student"+str(i) for i in range(1,11)]
name

genderlist = ['M', 'F']

import numpy as np

gender = np.random.choice(a=genderlist, size=10)
gender

marks1 = np.random.randint(0, 100, size=10)
marks1

marks2 = np.random.randint(0, 100, size=10)
marks2



pd5 = pd.DataFrame({'rollno':rollno,'name':name,
                    'gender':gender, 'marks1':marks1,
                    'marks2':marks2})

pd5



import pandas as pd

rollno = pd.Series(range(1,1000001))

name =[]
for i in range(1,1000000):
    name.append("Student"+str(i))
name

name = ["Student"+str(i) for i in range(1,1000001)]
name

genderlist = ['M', 'F']

import numpy as np

gender = np.random.choice(a=genderlist, size=1000000)
gender

marks1 = np.random.randint(0, 100, size=1000000)
marks1

marks2 = np.random.randint(0, 100, size=1000000)
marks2



pd5 = pd.DataFrame({'rollno':rollno,'name':name,
                    'gender':gender, 'marks1':marks1,
                    'marks2':marks2})

pd5.to_csv('Randomdata.csv', index=False)









import pandas as pd

rollno = pd.Series(range(1,11))

name =[]
for i in range(1,11):
    name.append("Student"+str(i))
name

name = ["Student"+str(i) for i in range(1,11)]
name

genderlist = ['M', 'F']

import numpy as np

gender = np.random.choice(a=genderlist, size=10)
gender

marks1 = np.random.randint(0, 100, size=10)
marks1

marks2 = np.random.randint(0, 100, size=10)
marks2



pd5 = pd.DataFrame({'rollno':rollno,'name':name,
                    'gender':gender})
pd5

course = np.random.choice(a=['BBA','MBA','BTECH'], size=10)
course

pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks2':marks2})
pd6

fees = pd.DataFrame({'course':['BBA','MBA','BTECH', 'MTECH'], 'fees':[100000, 200000, 150000, 220000]})
fees

pd5
pd6

fees


pd7 = pd.merge(pd5, pd6)
pd7
fees
pd8 = pd.merge(pd7, fees)
pd8

pd5 = pd5[:5]
pd5
pd6

rollno1 = pd.Series(range(6,16))

pd9 = pd.DataFrame({'rollno':rollno1, 'course':course, 'marks2':marks2})
pd9
pd5

pd10 = pd.merge(pd5, pd9, how='inner')
pd10

pd11 = pd.merge(pd5, pd9, how='outer')
pd11

pd12 = pd.merge(pd5, pd9, how='left')
pd12

pd13 = pd.merge(pd5, pd9, how='right')
pd13


pd14 = pd.DataFrame({'rollno1':rollno1, 'course':course, 'marks2':marks2})
pd14
pd5

pd15 = pd.merge(pd5, pd14, how='inner', left_on='rollno', right_on='rollno1')
pd15
pd15.drop(['rollno1'], axis=1)





import pandas as pd
import numpy as np

rollno = pd.Series(range(1,1001))

rollno

name = pd.Series(["student" + str(i) for i in range(1,1001)])
name

genderlist  = ['M','F']

import random
#gender = random.choices(genderlist, k=1000)
gender= np.random.choice(a=genderlist, size=1000,replace=True, p=[.6,.4])
gender


import collections

collections.Counter(gender)

marks1 = np.random.randint(0,100,size=1000)

marks2 = np.random.randint(0,100,size=1000)

fees = np.random.randint(50000,100000,size=1000)

fees.mean()

course = np.random.choice(a=['BBA','MBA','BTECH', 'MTech'], size=1000, p=[0.4, 0.5,0.09,0.01])

course
collections.Counter(course)

city = np.random.choice(a=['Delhi', 'Gurugram','Noida','Faridabad'], size=1000, replace=True, p=[.4,.2,.2,.2])

collections.Counter(city)


course = np.random.choice(a=['BBA','MBA','BTECH', 'MTech'], size=1000, p=[0.4, 0.5,0.09,0.01])
pd8 = pd.DataFrame({'rollno':rollno, 'name':name, 'course':course, 'gender':gender, 'marks1':marks1,'marks2':marks2, 'fees':fees,'city':city})
pd8














