fileName = input("Enter file name: ")
f = open(fileName, "r")
# Open file for input


lines=0
mostWordsInLine = 0



for lineOfText in f.readlines():
    wordCount = 0
    lines += 1

    f1=lineOfText.split()
    wordCount=wordCount+len(f1)
    if len(f1) > mostWordsInLine:
        mostWordsInLine = len(f1)
    print ((str(lineOfText)),str(wordCount))
