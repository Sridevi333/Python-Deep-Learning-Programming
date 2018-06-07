import random
while 0==0:
 n= random.randint(0,9)
 print('guess', n)
 n1=input("Enter a guess")
 guess=int(n1)
 if guess == n:
     print("Your answer is PERFECT!! Congratulations!!")
     break
 elif guess > n:
        print("Your answer is high than  required")
 else:
        print("Your answer is low than  required")