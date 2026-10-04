#  Factorial — Calculate the factorial of a number using a loop./

number = int(input("Enter your number:"))

factorial = 1

for i in range(1, number+1):
    factorial = factorial*i

    print("Factorial:", factorial)