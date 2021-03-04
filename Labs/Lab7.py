#!/usr/bin/env python
# coding: utf-8

# In[48]:


from flashtext import KeywordProcessor


# In[178]:


keywordprocessor = KeywordProcessor()
keywordprocessor.add_keyword("Noah")
Text = "Noah is going to make the world a bette place, Noah will own all of the coca cola in the world and Noah will build a empire based off choclate. Noah is great"
Extractedkeywords = keywordprocessor.extract_keywords(Text)
print(Extractedkeywords)


# In[179]:


#####################################################################################################################


# In[180]:


keywordprocessor.add_keyword("Noah", "John")
TextN = "Noah is going to make the world a bette place, Noah will own all of the coca cola in the world and Noah will build a empire based off choclate. Noah is great"
new_text1 = keywordprocessor.replace_keywords(TextN)
print(new_text1)


# In[116]:


#########################################################################################################################


# In[200]:


keywordprocessor = KeywordProcessor()
keywordprocessor.add_keyword("Noah")
Text = "Noah is going to make the world a bette place, Noah will own all of the coca cola in the world and Noah will build a empire based off choclate. Noah is great"
Extractedkeywords = keywordprocessor.extract_keywords(Text)
print(Extractedkeywords)


# In[ ]:





# In[ ]:




