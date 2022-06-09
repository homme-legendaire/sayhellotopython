def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def countEvenNums(n):
    count = 0
    for i in range(1, n+1):
        if isEven(i):
            count += 1
    return count


n = int(input())
print("The number of evens is", countEvenNums(n))
