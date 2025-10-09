#vote

age = int(input("enter the age "))

if(age>=18):
    print("elgible for voting")
else:
    print("not eligible for voting")
    leftage = 18-age
    print(leftage,"years is left for eligiblity")