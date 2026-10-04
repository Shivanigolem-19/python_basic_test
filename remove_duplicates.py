# Remove Duplicates — Remove duplicate values from a list without using set(). Example: [1,2,2,3,4,4,5] → [1,2,3,4,5]

number = [1,2,2,3,4,4,5]

unique = []

for num in number:
    if num not in unique:
        unique.append(num)
print(unique)