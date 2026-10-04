# Character Frequency — For 'programming', print how many times each character occurs.

text = "programming"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)