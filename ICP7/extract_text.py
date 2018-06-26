from bs4 import BeautifulSoup #import package for web scraping
import urllib.request  #import url library
import os
import re
f = open('C:/Users/Sridevi/PycharmProjects/ICP7/input.txt','w')
url = "https://en.wikipedia.org/wiki/Python_(programming_language)" #define the url for the web scraping
source_code = urllib.request.urlopen(url)    #request the wiki url using url lib
plain_text = source_code   #assign the value
soup = BeautifulSoup(plain_text, "html.parser") #call the Beautifulsoup method for parsing wiki page html file
data = soup.find_all('p')
for word in data:
    #print(word.text)
    f.write(str(word.text))




