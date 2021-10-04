# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:03:30 2021

@author: vikas
"""

import pandas as pd

df = pd.read_csv('binary.csv')
df

df = df[['admit', 'gre']]

import matplotlib.pyplot as plt

plt.scatter(df['gre'], df['admit'])


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(df['gre'].values.reshape((-1,1)), df['admit'].values)

y_pred = model.predict(df['gre'].values.reshape((-1,1)))

plt.scatter(df['gre'], df['admit'])
plt.scatter(df['gre'], y_pred)


res = []

import numpy as np

for i in df['gre'].values:
    res.append((1)/(1+np.exp(-i)))

res

plt.scatter(df['gre'], df['admit'])
plt.scatter(df['gre'], y_pred)
plt.scatter(df['gre'], res)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(df['gre'].values.reshape((-1,1)), df['admit'].values)

y_pred1 = model.predict_proba(df['gre'].values.reshape((-1,1)))

plt.scatter(df['gre'], df['admit'])
plt.scatter(df['gre'], y_pred)
plt.scatter(df['gre'], y_pred1[:,1])



import math

math.exp(10)

ls= list(range(-16,16))

y=[]
for x in ls:
    y.append((1)/(1+math.exp(-x)))


import matplotlib.pyplot as plt
plt.scatter(ls,y)


res = []

import numpy as np

for i in range(-100,100):
    res.append((1)/(1+np.exp(-i)))

res

plt.scatter(range(-100,100), res)







import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic_all_numeric.csv')
df.columns

x = df.drop('survived', axis=1).values
y = df['survived'].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
model  =  LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

from sklearn.metrics import confusion_matrix
cf = confusion_matrix(y_test, y_pred)
cf
Acc = (cf[0,0]+cf[1,1])/(cf[0,0]+cf[0,1]+cf[1,0]+cf[1,1])
Acc

from sklearn.metrics import accuracy_score, precision_score, recall_score
accuracy = accuracy_score(y_test, y_pred)
accuracy

'''
y_test = [1,1,1,1,0,1,0,1,1,1]
y_pred = [1,1,1,1,1,1,1,1,1,1]

accuracy = accuracy_score(y_test, y_pred)
accuracy

y_test = [0,0,0,0,0,0,0,0,0,0]
y_pred = [1,1,1,1,1,1,1,1,1,1]
'''
accuracy = accuracy_score(y_test, y_pred)
accuracy

precision = precision_score(y_test, y_pred)
precision

recall = recall_score(y_test, y_pred)
recall

from sklearn.metrics import roc_curve, roc_auc_score

y_pred_proba = model.predict_proba(x_test)[::,1]
y_pred_proba
y_pred_proba.shape

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

fpr 
tpr

auc = roc_auc_score(y_test, y_pred_proba)
auc

#together
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show();
auc
#AUC score for the case is 0.86. AUC score 1 represents perfect classifier, and 0.5 represents a worthless classifier.



import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

df = pd.read_csv('loan_data.csv')
df.columns

df = df.drop(['credit.policy', 'purpose'], axis=1)

x = df.drop('not.fully.paid', axis=1).values
y = df['not.fully.paid'].values

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

#oversample = SMOTE()
#x, y = oversample.fit_resample(x, y)
under = RandomUnderSampler(sampling_strategy=0.9)
x, y = under.fit_resample(x, y)

pd.Series(y).value_counts()


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
model  =  LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score, precision_score, recall_score
accuracy = accuracy_score(y_test, y_pred)
accuracy

precision = precision_score(y_test, y_pred)
precision

recall = recall_score(y_test, y_pred)
recall

from sklearn.metrics import roc_curve, roc_auc_score

y_pred_proba = model.predict_proba(x_test)[::,1]
y_pred_proba
y_pred_proba.shape

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

fpr 
tpr

auc = roc_auc_score(y_test, y_pred_proba)
auc

#together
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show();
auc
#AUC score for the case is 0.86. AUC score 1 represents perfect classifier, and 0.5 represents a worthless classifier.



from sklearn.tree import DecisionTreeClassifier

model










