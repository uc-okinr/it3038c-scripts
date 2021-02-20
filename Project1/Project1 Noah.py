#!/usr/bin/env python
# coding: utf-8

# In[8]:


# This script allows you to input a Wikipedia link in which the ouput will be The title/topic and the table of contents of that page
# I imported two libraies, BeautifulSoup, and request to complete this

from bs4 import BeautifulSoup
import requests

URL = input('Wikipedia Website Link: '  
           )

page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')


title = soup.find(id='firstHeading')
print()
print("Topic: " + str(title.text))

results = soup.find('div', id='toc')

contents = results.find_all("ul")
print()
print("Table of Content")
print()

# This is not perfect. Because i can't figure how just get the text and not the numbers.
# Also another issue is if there is more than 2 sub levels the script essentially wont pick them up, Need to figure that out


for content in contents:
    head = content.find('span', class_= 'toctext')
    sub= content.find('li',class_='toclevel-2' )
    if None in (head, sub):
        continue
    print(head.text)
    print(sub.text)



    

    
# These are my references

#https://stackoverflow.com/questions/53980144/nonetype-object-has-no-attribute-text-in-beautifulsoup

#https://towardsdatascience.com/step-by-step-tutorial-web-scraping-wikipedia-with-beautifulsoup-48d7f2dfa52d

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find

#https://www.youtube.com/watch?v=ng2o98k983k&t=2115s

#https://realpython.com/python-web-scraping-practical-introduction/




# In[ ]:




