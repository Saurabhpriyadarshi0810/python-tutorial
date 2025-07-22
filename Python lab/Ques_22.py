#find prime number between m and n 

def prime (m , n ):
    for i in range(m,n):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i,"is a prime number")
  
  
num1 =  int ( input ("enter the lower range :") )
num2 =  int ( input ("enter the upper range :") )

prime(num1 , num2)