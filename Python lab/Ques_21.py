# finding factorial using function

def factorial (num):
    fact =  1
    for i in range(1,num):
        fact *= i 
    return fact

num = int (input("enter the number"))

print("factorial of ",num,"is",factorial(num))
