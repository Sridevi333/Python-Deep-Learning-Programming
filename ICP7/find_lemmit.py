#import naturallanguage toolkit for lemmitizer and stemming
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

#load input file
input_data=open('input.txt',"r+")
#read the line from input data
data=input_data.read()
#tokenize each word from the line
words=word_tokenize(data)
#apply lemmatizer model
lemm=WordNetLemmatizer()
#iterate each word and print the lemmatize for word
for k in words:
    print("Lemmatizor for word "+k+" is "+lemm.lemmatize(k))