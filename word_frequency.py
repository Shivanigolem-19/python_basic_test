#  Word Frequency — For 'python is easy and python is powerful', count the frequency of every word.

text = "python is easy and python is powerful"

words = text.split()

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i]= 1
print(frequency)