# count number of digits in a number

num = int ( input("enter a number"))
num_given = num
count = 0

while(num >0):
   last_digit = num %10
   count += 1 
   num =  num//10
   
print("number of digits in ",num_given,"is",count)