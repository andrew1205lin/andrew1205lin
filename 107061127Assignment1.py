#!/usr/bin/env python
# coding: utf-8

# In[2]:


MTotal=input('How much money do you have?')
Process=input('Add an expense or income record with description and amount:')
SProcess=Process.split(' ')
print("Now you have %d dollars." %  (int(MTotal)+int(SProcess[1]))  )


# In[ ]:




