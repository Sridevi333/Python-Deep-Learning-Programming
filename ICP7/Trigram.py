#import nltk for trigrams and wordtokens
from nltk.util import trigrams
from nltk.tokenize import word_tokenize
#load input file
input=open('input.txt','r')
#read the data
line =input.read()
#get word tokens
token= word_tokenize(line)
#iterate each line and get trigrams
for x in trigrams(token):
    print(x)