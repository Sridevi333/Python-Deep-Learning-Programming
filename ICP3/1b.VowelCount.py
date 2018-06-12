userstring = input("Enter a string: ")
count = 0
vowels = set("aeiou")
#iterating through the input string and icrementing the count if one of the vowel is present
for letter in userstring:
    if letter in vowels:
        count += 1
print ("Vowel  count:" ,count)