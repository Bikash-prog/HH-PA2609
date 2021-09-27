# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 20:21:51 2021

@author: vikas
"""

#string by default

print()
print("Welcome")
print("To Python")


print ("Welcome", "to", "Python")
print ("Welcome", "to", "Python", sep='0')


print ("Welcome", "to", "Python", end='-----')
print ("Welcome", "to", "Python", sep='0', end='-----')
print ("Welcome", "to", "Python", sep='0')

print?
help(print)


import pandas

help(pandas)


import pandas as pd

help(pd)

help(pandas)


import pandas

pandas.__version__

import pandas as pd
pd.__version__


!pip install pandas
!conda install pandas

country ="India"

print ("India")

print (country)
print (count)


'''
this is an 
integer
'''
#this is an integer
a = 50


'''
int a;
a= 50;
'''


#Demonstrate the Positional Change of Indexes of Arguments
a = 10
b = 20

print ("The value of a is ", a, " and value of b is ", b , sep= '-')

print ("The value of a is {0} and value of b is {1}".format(a,b), sep= '-')

print ("The value of a is {1} and value of b is {0}".format(a,b), sep= '-')


country = input(" Enter Your Country Name -> ")

a = int(input("Enter value of a -> "))


# Integer , 2, 100, 1009
# Float, 5.6, 8.0001, 0.000001
# String, Vikas2020, Python

a =10
b =20

a+b

"print " + " Python"

f = 3.5

f_i = int(f)
f_s = str(f)

print("Print Float "+ str(f))

i = 3

i_f = float(i)
i_s = str(i)


s= "10"
s = "Marks 10"
a = int (s[6:8])
b=20
a+b


s= "10"

s_f = float(s)
s_i = int (s)


a= 64
chr(a)

s = 'a'
ord(s)

ch =  input("Enter a Char-> ")
if (ord(ch)>=97 and ord(ch)<=122):
    print("OK")
else:
    print("Not OK")


x = 3

print(x)

print (type(x))

print(x+1)
print(x*1)
print(x/2)
print(x-2)
print (x ** 3)

print(x)

x = x + 1 

x = x ** 3


print(x, x+1, x-2, x**3, x*3)


#Boolean
t = True
f = False

a = 10
a == 11
a > 10
a >= 10
a < 10
a <= 10
b = a != 10


a= True
if (a == True):
    print ("OK")


for i in range(1, 100):
    print(i)


Marks = int(input("Enter Marks -> "))
course = input("Enter Course -> ")

output= Marks > 75 and course == "HR"

print("Output is -> ", output)

'''
AND
X Y O
0 0 0
0 1 0
1 0 0
1 1 1
'''


Marks = int(input("Enter Marks -> "))
course = input("Enter Course -> ")

output= Marks > 75 or course == "HR"

print("Output is -> ", output)

'''
OR
X Y O
0 0 0
0 1 1
1 0 1
1 1 1
'''

'''
NOT

X O
0 1
1 0
'''
a = True

print (not(a))


Fname = 'Vikas'
Lname = 'Khullar'

name  = Fname + Lname

name  = Fname + ' ' + Lname

h = 'hello'
w = 'world'

h.capitalize()
h = h.upper()
h

h.lower()

h
h.rjust(10)

h.ljust(10)

h.center(10)


h = "Java is an easy PL"

h.replace('Java', 'Python')

h.replace(' ', '-')

name = input("Enter Your Name -> ")

print(name)

name1 = name.strip()


name = 'Name'

name =  "Name's"


array = {10, 20, 30, 40}

# List, Set, Dictionary, Tuple

# Hetrogeneous, Ordered, Unqiueness, Mutable, indexed


l1 = []

l1 = [1,2,3,7,6,5]
# Non Ordered Dtype

print(l1)

#indexed

l1[5]

#Hetrogeneous


l2 = ['Vikas', 1, 54.33, True]
print(l2)


# Indexed
l2[0]
l2[2]
l2[3]
l2[4]


r1 = range(101)
l3 = list(r1)
l3

r1 = range(10, 101)
l3 = list(r1)
l3

r1 = range(10, 101, 5)
l3 = list(r1)
l3

r2 = range(0, 100000000)
l4 = list(r2)
l4


l4[0]
l4[1]

l3

'''
for i
{
    print(); 
}
'''

for i in l3:
    print(i+10)


#Mutable or changable

l2

l2[0] = 'Kumar'
l2

l2.append('Vicky')
l2

l2.append(1)
l2

# Not Uniqueness

l2.pop()

l2

l2.pop(0)
l2

l2.insert(2, "ABC")
l2

l1
l1.sort()
l1

l1.reverse()
l1


l1 = list(range(1, 1000000))
l1.reverse()
l1


l2.remove('Vicky')
l2

l2



l3 = [1,2,4,3,5,7,1,2,9,7,4,4]
l3.count(4)


import pandas as pd
df = pd.read_csv('binary.csv')
df.columns
l5 = list(df['admit'])


l5.count(0)
l5.count(1)


l5.clear()

del l5


l6 =  list(range(100,120))
l6

l6[1]
l6[0]
l6[19]


l6[0:6]

l6[:5]

l6[4:]

l6[4:8]

l6[0]
l6[-1]

l6[-5:]

fruits = ['apple', 'banana', 'cherry']


for i in fruits:
    print("00000")
    print (i)

x = iter(fruits)

print(next(x))
print("00000")
print("00000")
print("00000")

print(next(x))
print("00000")
print("00000")

print(next(x))
print("00000")
print("00000")
print("00000")
print("00000")


#Set

#Mutable, Not Indexed, Ordered, Hetrogeneous, Uniqueness


s1 = {0,1,4,3,6,7,2}
#ordered

s2 = {0,1,1,6,5,6,9,8,7,8,9}
# Uniqueness

s2[1]
# Not Indexed


#Mutable
s2
s2.pop()
s2

s2.add(11)
s2.add(9)

s2.remove(7)
s2

s2.update([10, 22, 4, 66,77])
s2


for i in s2:
    print(i)


x = iter(s2)

next(x)


integer 4 Bytes

1000000*4 / 1024 /1024



l1 = list(range(1,10))

l2 = l1

l1[5]=55

l2[4]= 66

l3 = l1.copy()

l1 [2] =33

l3[3]=99



teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}

teamA.union(teamB)

teamA.intersection(teamB)

teamA.difference(teamB)


#Dictionary

#Not indexed, # Key: Value Pair, hetrogeous
d1 = {}
d1= {'roll':1, 'name': 'Vikas'}

car = {'brand': 'Honda', 'model': 'Jazz', 'year':2021}

#Not indexed
car[1]

car['brand']

car['model']

car.get('model')

#mutable
car

car['color'] ='Black'
car

car['color']= 'white'
car


car.keys()
car.values()

for i in car.keys():
    print(i)


for i in car.values():
    print(i)

car.items()

for i in car.items():
    print(i)


for i, j in car.items():
    print(i)
    print(j)

car

car.pop('color')

car

car.popitem()

car.clear()

del car 


#List           Mutable, Indexed, Unorderd, collection, square bracket
#Dictionary     Mutable, key-value paired, Unorderd, collection, curly bracket
#Tuples -       unmutatble, collection, ordered, round bracket

t1 = ()

t1 = (0,4,3,6,5,8,5,4,8)

#Not Ordered

t1[0]
#indexed


t1[0] = 22
#Not Mutable

t1.count(8)

#hetrogeneous

t2 = ('Vikas', 12, 3.5, True)

t2[0] ='Vicky'

t1 = (1, 5)

(1, 5, 4)

(1, 5) + 4





























