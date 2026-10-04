#  Anagram — Check whether two strings are anagrams. Example: listen and silent → Anagram./

A = "listen"
B = "silent"

if sorted(A) == sorted(B):
    print("Anagram")
else:
    print("Not anagram")