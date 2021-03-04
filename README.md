# it3080c-scripts


**My Github repo for IT3080C

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
