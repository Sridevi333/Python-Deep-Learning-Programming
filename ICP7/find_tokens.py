#import nltk for word tokens
from nltk.tokenize import word_tokenize
#load the input file
input_data=open('input.txt',"r+")
#read the data
data=input_data.read()
#print the tokens
print("Tokenization: ",word_tokenize(data))
