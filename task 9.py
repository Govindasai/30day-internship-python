#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c = lambda a,b:a*b
print(c(a,b))


# In[3]:


limit = int(input('enter the limit of fibonacci series'))
fibonacci_list = [0,1]
first = 0
second = 1
while len(fibonacci_list) < limit:
        expression = lambda fi,se:first+second
        append = expression(first, second)
        fibonacci_list.append(append)
        first = second
        second = append
print(fibonacci_list)


# In[4]:


given_number = int(input("enter the number to multiply by"))
given_list = [4,5,3,7,8]
multiply_list = []
for i in given_list:
    expression = lambda i,gn : i*given_number
    multiply_list.append(expression(i,given_number))
print(multiply_list)


# In[5]:


task_list = [27,19,16,18,24]
divisible_list = []
for i in task_list:
    if (i%9) == 0 :
        divisible_list.append(i)
print(divisible_list)


# In[6]:


task_list = [4,2,5,6,7,8,9,22]
even_list = []
for i in task_list:
    if i%2 == 0:
        even_list.append(i)
print(even_list)


# In[ ]:




