num = int ( input ("enter the number "))

negative = 0
positive = 0
zero = 0

while ( num != -1):
    if(num>0):
        positive += 1
    elif(num<0):
        negative += 1
    elif(num == 0):
        zero += 1
    num = int ( input ("enter the number "))
    
print("positive no entered =",positive)
print("negative no entered =",negative)
print("zeros entered =",zero)