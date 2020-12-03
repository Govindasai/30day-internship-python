#!/usr/bin/env python
# coding: utf-8

# In[1]:


x1=["sai","joe","david"]
x2=["panda","mash","harsh"]
converted_tuples=zip(x1,x2)
converted_lists=list(converted_tuples)
print(converted_lists)


# In[2]:


task_list=["sai","mash","panda","harsh"]
range_list=[1,2,3,4,5,6,7,8]
converted_list=list(zip(range_list,task_list))
print(converted_list)


# In[3]:


task_list = [4,3,6,2,7,8]
sorting_list=sorted(task_list,reverse=False)
print(sorting_list)


# In[4]:


numbers_list = [3, 4, 2, 5, 6, 7, 9, 23, 22, 14]
odd_list = []


def logic(i):
    if i % 2 == 0:
        return False
    else:
        return True


filter_list = filter(logic,numbers_list)
for number in filter_list:
    odd_list.append(number)
print(odd_list)


# In[ ]:




