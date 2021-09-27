# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:01:34 2021

@author: vikas
"""

#Conditions
'''
if (conditional statement -> True)
{
    Perform Line of Statements
    Perform Line of Statements
    
    Perform Line of Statements
}
'''

a = 10
b = 20

if (a > b):
    print ("a is greater than b")


if (a>b):
    print ("a is greater")
else:
    print("b is greater")
    
    
marks = int(input("Enter Marks -> "))

if (marks > 90):
    print("A")
elif (marks>80 and marks <=90):
    print ("B")
elif (marks>70 and marks <=80):
    print ("C")
elif (marks>60 and marks <=70):
    print ("D")
else:
    print ("F")

   

#Looping

for i in list(range(0,50,5)):
    print(i)

name =[]
for i in list(range(0,5)):
    n = input("Enter Name -> ")
    name.append(n)


name =[]
n = input("Enter Name -> ")
name.append(n)

n = input("Enter Name -> ")
name.append(n)

n = input("Enter Name -> ")
name.append(n)

n = input("Enter Name -> ")
name.append(n)

n = input("Enter Name -> ")
name.append(n)


for i in range(1,11):
    print("2 * {0} = {1}".format(i, 2*i))


print (j , " * ", i, " = ", j*i)

print (str(j) + " * " + str(i) + " = "+  str(j*i)

for j in range(1, 11):
    for i in range(1,11):
        print("{0} * {1} = {2}".format(j, i, j*i))


l2 = ['name', 'rno', 'branch']

data = []
for j in range(1, 6):
    l3=[]
    for i in range (0, 3):
        l3.append(input("Enter detail {0}- >".format(l2[i])))
    data.append(l3)

data


choice = 1

while (choice):
    l3=[]
    for i in range (0, 3):
        l3.append(input("Enter detail {0}- >".format(l2[i])))
    data.append(l3)
    choice  = int(input("Enter 1 for more details or enter 0 -> "))

data



while(True):
    print("Aa")


cnt=0
while(cnt<10):
    print("Aa")
    cnt = cnt + 1

team = ['India', 'Australia','Nepal', 'England']   # 4elements   list index 0-3

for i in team: 
    print(i)



#Break

for i in team:
    if i == 'Nepal':
        print (i, " In Condition ")
        break
    print (i, " Outer Condition")
    


#Continue

for i in team:
    if i == 'Nepal':
        print (i, " In Condition ")
        continue
    print (i, " Outer Condition")
    



l2 = ['name', 'rno', 'branch']

data=[]
while (True):
    l3=[]
    for i in range (0, 3):
        l3.append(input("Enter detail {0}- >".format(l2[i])))
    data.append(l3)
    choice  = int(input("Enter 1 for more details or enter 0 -> "))
    if choice == 0:
        break




data=[]
cnt=0
while (True):
    l3=[]
    while(cnt<3):
        det= input("Enter detail {0}- >".format(l2[cnt]))
        if (det==''):
            continue
        cnt = cnt +1
        l3.append(det)
    data.append(l3)
    choice  = int(input("Enter 1 for more details or enter 0 -> "))
    if choice == 0:
        break


#Functions

a = 10
b =20

def oper():
    print( a+b)
    print (a-b)
    print (a*b)

oper()

oper()

oper()



def printHello():
    print ("Hello")

printHello()

printHello()

printHello()



def printHello(name):
    print ("Hello " + name)

printHello("Vikas")

printHello("AK")

printHello("VK")



def printHello(fname, lname):
    print ("Hello " + fname +" "+ lname)

printHello("Vikas", "Khullar")

printHello("AK", "Kumar")

printHello("VK", "Gupta")


def dat(name, rno, branch= 'None'):
    print (name, rno, branch)


a = dat("vk", 22, 'CSE')
a

dat("vk", 22)


def dat1(name, rno = 'None', branch= 'None'):
    print (name, rno, branch)
    return(name, rno, branch)

a = dat1("VK", 111, 'CSE')
a


def maximum(l1):
    m=0
    for i in l1:
        if (m<i):
            m=i
    return (m)


lst = [6,5,3,8,1]
maximum(lst)

lst.sort()
lst



data=[]
def dat1():
    l1=[]
    l1.append(input('Enter Name -> '))
    l1.append(input('Enter Rno -> '))
    l1.append(input('Enter Branch -> '))
    return(l1)



for i in range(0,5):
    l1 = dat1()
    data.append(l1)




l1 = dat1()
data.append(l1)

data


l1 = dat1()
data.append(l1)

l1 = dat1()
data.append(l1)



# Lambda

def f(x):
    return(x**2)


f(2)

f(9)


fl = lambda x : x**2

fl(10)


fl1 = lambda x,y: (x+y, x-y)

fl1(10,20)

l1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

lm1 = lambda x: x*2
l2=[]
for i in l1:
    l2.append(lm1(i))
l2


#map, filter, reduce
l1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , l1)) 
print(final_list)


l1 = list(range(1, 10))
l1
fl = list( map(lambda x: x+2, l1))

fl


l1 = [5, '', 22, 97, '' , 62, 77, '', 73, 61] 
final_list = list(filter(lambda x: (x != '') , l1)) 
print(final_list) 


l1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

final_list = list(filter(lambda x: (x > 50) , l1)) 
print(final_list) 


x =9
x/2

x % 2



l1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 == 0) , l1)) 
print(final_list) 



from functools import reduce

li = [5, 8, 10, 20, 50, 100] 

s1 = reduce(lambda x, y: x * y, li) 

print (s1) 


import random as rd

x = rd.randint(1, 100)
x

l1 = [111,222,333,444,555,666]

rd.choice(l1)

rd.choices(l1, k=3)


gender = ['M', 'F']

lst = rd.choices(gender, k=100)

len(lst)





































































































