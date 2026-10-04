#  Find Duplicates — Find all duplicate elements in a list.

number = [1,2,2,3,4,4,5,6]

duplicate = []

for num in number:
    if number.count(num) > 1 and num not in duplicate:
        duplicate.append(num)
print(duplicate)