#finding max  of three number using function

def comparision (a , b , c ):
    if(a>b and a>c):
        print(a,"is greater than",b,"and",c)
    elif(b>a and b>c):
        print(b,"is greater than",a,"and",c)
    elif(c>a and c>a):
        print(c,"is greater than",a,"and",b)
        
num1 = int(input("enter  first number :"))
num2 = int(input("enter  second number :"))
num3 = int(input("enter  third number :"))

comparision(num1 , num2 , num3 )