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








































































