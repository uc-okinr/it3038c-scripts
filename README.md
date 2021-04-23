# it3080c-scripts


**My Github repo for IT3080C

Project 1

# This script allows you to input a Wikipedia link in which the ouput will be The title/topic and the table of contents of that page
# I imported two libraies, BeautifulSoup, and request to complete this
# This is not perfect. Because i can't figure how just get the text and not the numbers.
# Also another issue is if there is more than 2 sub levels the script essentially wont pick them up, Need to figure that out

Project 2
    
# My goal was to plant a table using panda, but ran into some issues. I tried to use this link "https://en.wikipedia.org/wiki/List_of_Japanese_military_equipment_of_World_War_II"
#Again could'nt quite get it to run right so turning it in how ti is

Project 3

# Used several different python packages. Seaborn, and Panda. These tools are mainly used for data science and visualization.
# Just make sure to download the appropriate packages.
# All you would have to is make sure to have downloaded csv that the code would pull from and then run it.

# https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset
# You can use kaggle, for finding CSV file



















Lab 7 Example 

Here is my example for my code for Lab 7, My sandbox isnt working properly right now so i used my own VM using mint OS. I used Jupyter Notebook as my enviroment. So to start you need to install FlashText,

apt-get install Flashtext

**Now by following this template all you need to do is Add some Text and a Key word that you want to Track. FlashText will then find the word and display how many times that word is used in the Text**


from flashtext import KeywordProcessor

keywordprocessor = KeywordProcessor()
keywordprocessor.add_keyword(" <word> ")
Text = "<Words or sentences>"
Extractedkeywords = keywordprocessor.extract_keywords(Text)
print(Extractedkeywords)
  
  **We can also replace the keyword we have chosen with another word and display the results
  
  keywordprocessor.add_keyword("<Word>", "<Replacement>")
TextN = "<words or Sentence>"
new_text1 = keywordprocessor.replace_keywords(TextN)
print(new_text1)
  
  **We can also display the number of times that Keyword displays itself with a simple additon to the code**
  
  keywordprocessor = KeywordProcessor()
keywordprocessor.add_keyword("<>")
Text = "<>"
Extractedkeywords = keywordprocessor.extract_keywords(Text)
print(lens(Extractedkeywords))
