# wap to count occurance of a character in a string 

s = input("Enter a string: ")
ch =input("enter a character:")

count = 0

for char in s:
    if (char== ch):
       count += 1

print("there are",count,ch ," in string")