#fibbonaci series

term = int ( input ("enter number of terms:"))
first = 0
second = 1

if term == 1:
    print(first)
elif term == 2 :
    print(first)
    print(second)
elif  term > 2 :
    print(first)
    print(second)
    i = 3
    while i <= term:
        next_term = first + second 
        print(next_term)
        first = second 
        second = next_term
        i += 1