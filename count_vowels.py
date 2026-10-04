#  Count Vowels — Count the number of vowels in a string.

a = input("Enter your choice:")

b= a.lower()

count=0

for char in b:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)