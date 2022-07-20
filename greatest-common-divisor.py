#wylicz najwiekszy wspolny dzielnik dla a i b

#greatest common divisor - NWD

a=int(input("Enter number 'a': "))
b=int(input("Enter number 'b': "))

while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("The greatest common divisor is: ", a)


#   OR with a function:

def greatest_common_divisor(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print(greatest_common_divisor(15,5))
