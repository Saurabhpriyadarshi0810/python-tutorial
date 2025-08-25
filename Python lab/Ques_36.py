# 36

alist=[]
for i in range (1,11):
    alist.append(i)

print(alist)

for i in alist:
    if ( i % 2 == 0):
        alist.remove(i)

print(alist)
