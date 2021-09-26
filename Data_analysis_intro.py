#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3])
print(a)
print(a.shape)


# In[5]:


print(a[0],a[1],a[2])
a[0]=5
print(a)


# In[10]:


b = np.array([[1,2,3],
              [4,5,6]])
print(b)
print(b.shape)


# In[11]:


print(b[0,0])


# In[16]:


a = np.zeros((2,3))
print(a)
b = np.ones((3,4))
print(b)
c = np.full((2,3),7)
print(c)


# In[17]:


e = np.random.random((3,3))
print(e)


# In[18]:


a =np.array([[1,2],[3,4],[5,6]])

print(a)


# In[19]:


print(a>2)


# In[21]:


print(np.sum(a))


# In[23]:


print(np.sum(a, axis=0))


# In[24]:


print(np.sum(a, axis=1))


# In[26]:





# In[ ]:




