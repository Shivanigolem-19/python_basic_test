# Fibonacci Series — Print the first n Fibonacci numbers. Example: 0 1 1 2 3 5 8 13.

a=0
b=1
for i in range(9):
    print(a)
    temp=a
    a=b
    b=temp+b