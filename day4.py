# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:52:07 2021

@author: vikas
"""

ls = ["vikas is teaching Python","vikas is teaching Python","vikas is teaching Python"]

for i in ls:
    spl = i.split(' ')
    print(spl)
    for j in spl:
        for k in range(0,len(j)):
            print(j[k])


s = 'Vikas'

for k in range(0, len(s)):
    print (s[k])
    

import numpy as np

a = np.random.randint(0, 100)
a

n1 = np.random.randint(0, 100, size =10)

type(n1)

n1

n1.shape


x2 = np.random.randint(0,10, size=(2,3))

x2

x2.shape

x3 = np.random.randint(0, 10, size=(2,3,4))

x3

x3.shape


#indexed




x4 = np.random.sample(size=10)
x4
x5 = np.random.randint(0,10, size=10)
x5
x6 = x4*x5
x6

x1 = np.random.randint(0, 100, size =10)

x1
x1[0]
x1[:4]
x1[4:]
x1[-1]
x1[-3:]


x2 = np.random.randint(0, 10, size=(3,4))

x2

x2[0][0]
x2[0,0]

x2[0,:]

x2[:,0]

x2[1,1]

x2

x2[:, :3]

x2[:2,:]

x2[:2, :2]
x2

x2[-2:,-2:]


x1
x1[-2:]


x3
x3[0,:,:]

x3[1,-2:,-2:]



x4 = np.arange(20)
x4

x5 = np.arange(10,20)
x5

x6 = np.arange(10, 100, 5)
x6


x6.shape

x6.reshape(6,3)

x6.reshape(2,9)

x6.reshape(2,3,3)


x1.shape
x1 = x1.reshape(-1,1)
x1.shape



a = np.zeros((2,4))
a

b = np.zeros((2,4), dtype=int)
b

c = np.ones((2,4), dtype = int)
c


np.empty((2,4))

np.eye(4,4)

l1 = np.linspace(0, 1, num=10)
l1


n1 = np.random.randint(0, 100, size=10)

n1

max(n1)
min(n1)
np.std(n1)
np.mean(n1)
np.max(n1)
np.min(n1)

n1 = np.random.randint(0, 1000000, size=1000000)

len(n1)

np.max(n1)
np.std(n1)


np.floor([1.2,1.6])
np.ceil([1.2,1.6])

np.floor([-1.2,-1.6])
np.ceil([-1.2,-1.6])

np.round([1.2, 1.6])
np.round([-1.2, -1.6])

np.trunc([1.2, 1.6])
np.trunc([-1.2, -1.6])

np.trunc([-1.2, -1.6])
np.floor([-1.2, -1.6])


a = np.round([1.2222, 2.34355], 3)

a[0]
a[1]

np.ceil([1.2,1.6])
np.trunc([1.2,1.6])

np.ceil([-1.2,-1.6])
np.trunc([-1.2,-1.6])


n1 = np.random.randint(0,10, size=(3,4))

n2 = np.random.randint(0,10, size=(3,4))

n1
n2

np.concatenate([n1, n2], axis=0)
np.concatenate([n1, n2], axis=1)

n1
n2




n1 = np.random.randint(0,10, size=(3,4))
n2 = np.random.randint(0,10, size=(3,5))

n1
n2

n3 = np.concatenate([n1, n2], axis=0)
np.concatenate([n1, n2], axis=1)


n1
n2

n3 = np.stack((n1, n2))
n3.shape


n3 = np.concatenate([n1, n2], axis=0)
n3


np.split(n3, 2, axis=1)

n3
#upper and lower
upper, lower = np.vsplit(n3,[2])
upper  #first 2 rows
lower # last row
#left and right : hsplit line : 1st col
left, right = np.hsplit(n3,[3])
left
right


n3.min()
n3.max()
np.min(n3)

n3.min(axis=0)
n3.max(axis=0)

n3.max(axis=1)
n3

np.median(n3)
np.sum(n3, axis=1)

n3
np.equal(n3, 4)
np.sum(np.equal(n3, 4))


np.greater(n3, 4)
n3

np.less(n3,4)
n3

np.less_equal(n3,4)
np.greater_equal(n3,4)
n3 < 4
n3>=4

n3
np.sort(n3, axis=0)


l1 = [15,13,14,2,6,7,8]


sum(l1)/7

np.mean(l1)

l1.sort()
l1
np.median(l1)



import matplotlib.pyplot as plt
n4 = np.random.normal(100, 10, size = 1000)
n4

np.median(n4)
np.std(n4)

plt.hist(n4, bins=20)



l1 = [1,2,3,4]

np.array1(l1)





































































