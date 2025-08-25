# 37

alist = [1,2,3,4,5,6,7,8,9,1,2,1,1,1,1,3,4]
count = 0
num  = int ( input( "enter the number you want to find"))
for i in range(len(alist)):
    if ( alist[i] == num):
        print("index =",i)
        count+= 1
print(num,"occuered",count,"times")
