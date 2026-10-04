#  Armstrong Number — Check whether a number is an Armstrong number. Example: 153 → Armstrong; 123 → Not Armstrong.

a=int(input("Enter a number:"))

length = len(str(a))
sum = 0
temp = a

while temp>0:
    digit = temp%10
    sum = sum + digit**length
    temp = temp//10

if sum == a:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")