sentence = input("Enter the data for word count: ").split()
ls = []
for i in sentence:
#Appending the words with the count
    word_count = sentence.count(i)  # Pythons count function, count()
    ls.append((i,word_count))

#changing to dictionary format from key-value pair
mydict = dict(ls)

print ("Output:",mydict)

#sorting the output by key
print("Sorted Output:",dict(sorted(mydict.items())))