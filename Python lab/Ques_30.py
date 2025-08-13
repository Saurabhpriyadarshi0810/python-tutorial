# wap a program to remove vowels from a string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
res = ""

for ch in s:
    if ch not in vowels:
        res = res + ch

print("After removing vowels:", res)