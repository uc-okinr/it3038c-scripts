#!/usr/bin/env python
# coding: utf-8

# In[12]:


##I have started a new project, This projects uses seveal pakages including Panda, and Seaborn
## I started this based off my graduate school work

from pandas import Series, DataFrame
import pandas as pd
import seaborn as sns


# In[13]:


## Enter the data that you want, Has to be a CSV
data_df=pd.read_csv('cs448b_ipasn.csv')


# In[15]:


print(data_df.head(6))

#This is just to make sure you it works


# In[18]:


sns.jointplot(data_df['date'], data_df['l_ipn'])

## There are many types of data plots that you can do, I found this the most intresting visually


# In[11]:





# In[ ]:




