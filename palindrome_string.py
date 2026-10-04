# Palindrome String — Check whether a string is a palindrome without using [::-1].

text = "madam"

reverse = ""

for i in range(len(text) -1, -1, -1):
    reverse += text[i]

if reverse == text:
    print("palidrome")
else:
    print("not palindrome")