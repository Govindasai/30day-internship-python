#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    a=1/0
#zero division error is logic
except ZeroDivisionError as zd:
    print('the error of given programme is',zd)
#syntaxerror
except SyntaxError as syn:
    print('the error is ',syn)


# In[2]:


try:
    a= int(input('enter the value of a'))
    b= int(input('enter the value of b'))
    def add(a,b):
        print('the addition of given two numbers is',a+b)
    def sub(a,b):
        print('the substraction of two given numbers is',a-b)
    def div(a,b):
        print('the division of given two numbers is',a/b)
    def multi(a,b):
        print('the multiplication of two given numbers is',a*b)
    process=input('enter the application to perform +,-,*,/  \n')
    if(process == '+'):
        add(a,b)
    elif(process =='-'):
        sub(a,b)
    elif(process == '*'):
        multi(a,b)
    elif(process == '/'):
        div(a,b)
    else:
        print('invalid process input')
except ZeroDivisionError :
    print('the value of b cannot be zero')


# In[3]:


try:
    print(error)
except NameError as ne:
    print(ne)
except :
    print('your code has errors')


# In[4]:


we use try except to check for validation.
and also to find out the specificity of errors in the  big projects or programme
there is no need to use in small programmes


# In[5]:


try:
    a=input('enter the value of a')
except:
    print('your code has errors')


# In[ ]:




