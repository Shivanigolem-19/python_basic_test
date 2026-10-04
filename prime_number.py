#  Prime Number — Check whether a given number is prime.

num = int(input("Enter your number:"))

if num<=1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if i%num==0:
            print("It is not a prime number")
            break
print("It is a prime number")