# prime nummber between 20 to 50

for i in range(20,50):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i,"is a prime number")
