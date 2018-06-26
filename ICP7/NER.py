#import the modules pos,wordpunct&ne_chunk
from nltk import pos_tag,ne_chunk,wordpunct_tokenize
#load the input file
file1=open('input.txt','r')
#read each line
text =file1.readline()
#until end of lines apply NER for each word and print
while text!='':
 print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
 text=file1.readline()
