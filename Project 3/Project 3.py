#!/usr/bin/env python
# coding: utf-8

# In[53]:


##I have started a new project, This projects uses seveal pakages including Panda, and Seaborn
## I started this based off my graduate school work that i started a while ago. 
## Seaborn is a tool used for graphical data analayis


import seaborn as sns

# I used jupyter notebook for this assignment


# In[54]:


#You are able to upload several differetn types of datasets from seaborn that are already made.
## Using this can help you find you favorite

sns.get_dataset_names()

##This will display datasets that seaborn already have


# In[55]:


## Enter the data that you want,
tips = sns.load_dataset("tips")

## To make it easier i will continue to use the Tips dataset


# In[56]:


print(tips)

#This is just to make sure you it works and to see the dataset


# In[57]:


# This is used to create the visual

sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",)


# In[58]:


# Another graph example that we can use is the distirbution graph. This is an information graph

sns.displot(data=tips, x="total_bill", col="time", kde=True)


# In[59]:


car = sns.load_dataset("car_crashes")


# In[60]:


print(car)


# In[61]:


# Here is another example using the car crash data set

sns.distplot(car['total'])


# In[62]:


## References
## https://seaborn.pydata.org/introduction.html
## https://medium.com/analytics-vidhya/deep-dive-into-seaborn-meet-the-datasets-8d08755a320b
##
##


# In[ ]:




