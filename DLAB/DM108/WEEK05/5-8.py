
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[1:] = numbers[10:] + numbers[1:10]
print(numbers[1:])

