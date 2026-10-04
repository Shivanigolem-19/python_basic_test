# Sum of Digits — Input 5832 → Output 18.

num = int(input("Enter your number:"))

sum = 0

while num>0:
    digit = num%10
    sum = sum + digit
    num = num//10

print("Sum of Digits:", sum)