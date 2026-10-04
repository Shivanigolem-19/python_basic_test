# Two Sum — Given numbers = [2, 7, 11, 15] and target = 9, find the two numbers whose sum equals the target.

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])