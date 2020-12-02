#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
task_list=['azaz','amar','0829','0456','AmaZ']
pattern="[a-zA-Z0-9]"
for i in task_list:
    print(re.findall(pattern,i))


# In[7]:


import re
string='pattabhi'
pattern= 'ab'
print(re.search(pattern,string))


# In[6]:


import re
string='govindasai16'
pattern = '[0-9$]'
print(re.findall(pattern,string))


# In[8]:


import re
string= 'the numbers i like are 2,14,22,234'
search= re.finditer(r'([0-9]{1,3})',string)
lists = []
for i in search:
    lists.append(i)
print(len(lists))


# In[9]:


import re
string='GOVINDASAI'
pattern ='[A-Z]'
search=re.findall(pattern,string)
if len(search) < len(string):
    print('invalid input')
else:
    print('valid input')


# In[ ]:




