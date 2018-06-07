file = open("data2","r")
for i in file:
    l = len(i)
    file1 = open("output","a")
    file1.write(i[:-1]+","+str(l-1)+'\n')
file1.close()