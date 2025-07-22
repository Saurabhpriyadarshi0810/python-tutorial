# find cube  of 1 to  30 using function

def cube(x):
    return x**3 

for i in range(1,31):
     num = cube(i)
     print("cube of ",i,"is",num)