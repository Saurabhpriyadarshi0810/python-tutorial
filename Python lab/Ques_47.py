# Nested list storing toppers details [Name, Course, Marks]
toppers = [
    ["Arrav", "B.Sc", 92.6],
    ["Saurabh", "B.Tech", 85.5],
    ["Archi", "B.Tech", 95.9]
]

# Print original details
print("Original Toppers List:")
for t in toppers:
    print(t)

# Asking if user wants to edit
choice = input("\nDo you want to edit any detail? (yes/no): ").lower()

if choice == "yes":
    name = input("Enter the name of the student you want to edit: ")

    found = False
    for t in toppers:
        if t[0].lower() == name.lower():   # match ignoring case
            found = True
            print("\nWhat do you want to edit?")
            print("1. Name\n2. Course\n3. Marks")
            opt = int(input("Enter option (1-3): "))

            if opt == 1:
                t[0] = input("Enter new name: ")
            elif opt == 2:
                t[1] = input("Enter new course: ")
            elif opt == 3:
                t[2] = float(input("Enter new marks: "))
            else:
                print("Invalid option!")

    if not found:
        print("Student not found!")

# Print updated details
print("\nUpdated Toppers List:")
for t in toppers:
    print(t)











































# toppers = (("Arrav","Bsc" ,92.6) , ("Saurabh","B.tech" , 85.5) , ("Archi","B.tech",95.9))

# for i in toppers :
#     print(i)                  


# choice = input("Do you want to edit the details: ")

# if choice == "yes":
#     name = input ("enter the name of student that you want to edit : ")
#     new_name = input("enter the correct name :")
#     new_course = input("enter the correct course :")
#     new_aggregate =float( input("enter the correct aggregate :"))
#     i = 0
#     new_toppers=()
    
#     while i < len(toppers):
#         if toppers[i][0] == name:
#             new_toppers += ((new_name,new_course,new_aggregate),)
#         else:
#             new_toppers += (toppers[i],)
#         i += 1

# for i in new_toppers:
#     print(i,end=" ")
                          