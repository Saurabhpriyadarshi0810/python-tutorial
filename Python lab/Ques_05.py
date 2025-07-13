#ques_05

num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = int(input("enter 3rd number:"))

if(num1>num2 and num1>num3):
    print(num1,"is greater than",num2,"and",num3)
elif (num2>num3 and num2>num1):
     print(num2,"is greater than",num1,"and",num3)
elif (num3> num2 and num3>num1):
     print(num3,"is greater than",num1,"and",num2)
