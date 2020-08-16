#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def cross_entropy(Y,P):
    Y=np.array(Y)
    P=np.array(P)
    return -np.sum(Y*np.log(P)+(1-Y)*np.log(1-P))

Y=[1,1,0]
P=[0.8,0.7,0.1]

print(cross_entropy(Y,P))


# In[ ]:




