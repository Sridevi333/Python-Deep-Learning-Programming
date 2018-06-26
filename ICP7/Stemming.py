#import natural lang kit to import snowball stemmer
from nltk.stem import SnowballStemmer
#load the input file
input_data=open('input.txt',"r+")
#read the data
data=input_data.read()
words=data.split("\n")
words=data.split(" ")
#initialize the stemmer
stemm=SnowballStemmer('english')
#iterate each word and apply stem
for k in words:
  print("Stemmimg for word "+k+" is "+ stemm.stem(k))
