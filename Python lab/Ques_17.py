
# reverse a number  

num = int ( input("enter a number"))
num_given = num
rev_num = 0

while(num >0):
   last_digit = num %10
   rev_num = (rev_num*10) + last_digit
   num = int( num/10)
   
print("on reversing",num_given,"we get ",rev_num)