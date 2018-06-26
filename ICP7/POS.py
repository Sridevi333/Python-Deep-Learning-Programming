#import nltk for wordtokens,pos,nechunk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
#load input file
input = open('input.txt','r', encoding="utf-8")
#read the data
text = input.read()
#get token for each word
words = word_tokenize(text)
#apply pos for each word and print
print(ne_chunk(pos_tag(words)))