# WAP to check wheater the given input is  digit or lowercase or uppercase character  or a special character (" use if else ladder ")


ch = input("Enter a character: ")


if len(ch) != 1:
    print("Please enter only one character.")
else:

    if ch >= '0' and ch <= '9':
        print("It is a digit.")
    elif ch >= 'a' and ch <= 'z':
        print("It is a lowercase letter.")
    elif ch >= 'A' and ch <= 'Z':
        print("It is an uppercase letter.")
    else:
        print("It is a special character.")

