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
