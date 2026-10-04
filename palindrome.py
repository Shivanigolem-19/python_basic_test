#  Palindrome Number — Check whether a number is a palindrome. Example: 121 → Palindrome; 123 → Not Palindrome.

num = input("Enter a number:")

temp = num
A = num[::-1]

if temp == A:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")