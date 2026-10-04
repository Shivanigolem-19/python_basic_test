# Second Largest — Find the second-largest number in a list without using sort(). Example: [10, 5, 8, 20, 15] → 15.

list = [10, 5, 8, 20, 15]

largest = list[0]
second_largest = list[0]

for num in list:
    if num>largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)