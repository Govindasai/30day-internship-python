#!/usr/bin/env python
# coding: utf-8

# In[5]:


def work_insert(work):
    a = int(input("enter no to insert into list"))
    work.append(a)
    print(work)
    return


def work_delete(work):
    a = int(input("enter no to delete in list"))
    work.remove(a)
    print(work)
    return

work =[45,56,78,99,90]
work_insert(work)
work_delete(work)
minimum = min(work)
maximum = max(work)
print(minimum)
print(maximum)


# In[6]:


k=('u bloody hell')
print(k[::-1])


# In[7]:


k=('hello hai bye')
y=list(k)
print(type(y))


# In[ ]:




