#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    pass
    el=np.sum(np.exp(L))
    return [np.exp(item)/el for item in L]

L=[5,6,7]
S=[2,1,0]

print(softmax(L))
print(softmax(S))


# In[ ]:




