#!/usr/bin/env python
# coding: utf-8

# In[5]:


l = [10, 50, 75, 83, 98, 84, 32]
 
for i in l: 
    print(i+2) 


# In[7]:


i=5
while i>0:
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    print()
    i=i-1
    


# In[9]:


fib = [0,1]
a = 0
b = 1
for i in range(1,100):
    c = a + b
    a = b
    b = c
    fib.append(c)
print('the fibonacci sequence from 1 to 100',fib)


# In[10]:


n = int(input('enter the number to be verified: '))
sum =0
temp= n
while temp>0:
    digit = temp%10
    sum += digit ** 3
    temp //= 10

if n == sum:
    print( n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")


# In[11]:


multi_range = int(input("enter the limit of table number required"))
num = 1
multi_number=9
while (num <= multi_range):
    print(multi_number,'*',num,'=',multi_number*num)
    num += 1


# In[12]:


n = int(input('enter the number '))
if(n <0):
    print(n,'is negative')
else:
    print(n,"is positive")


# In[13]:


days_input = int(input('enter number of days'))
years = 0
if days_input > 364:
    while days_input >= 0 and days_input >= 365:
        years += 1
        days_input -= 365
print(years,'the years completed in days input')


# In[14]:


import math
def find_cos(num):
    cos = math.cos(num)
    print(cos)
theta = int(input("enter the theta value"))
find_cos(theta)


# In[15]:


num1=int(input('enter the first value'))
num2=int(input('enter the second value'))
action= input('press corresponding symbols for calculation')

if(action == '+'):
    print('addition of',num1,',',num2,'is',num1+num2)
elif(action == '-'):
    print('subtraction of',num1,',',num2,'is',num1-num2)
elif(action == '/'):
    print('division of',num1,',',num2,'is',num1/num2)
elif(action == '*'):
    print('multiplication of',num1,'and',num2,'is',num1*num2)


# In[ ]:




