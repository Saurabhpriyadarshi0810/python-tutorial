#38

alist = [ 1,2,3,4,5,6,7,8,9,10,1,1,1,2,2,3,3,3,5,6]
unique_list = []

for i in alist:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)