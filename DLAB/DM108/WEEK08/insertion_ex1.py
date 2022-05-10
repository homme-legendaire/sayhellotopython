def insertion(x):
    n = len(x)
    for i in range(1, n):
        j = i
        tmp = x[i]
        while j > 0 and x[j-1] > tmp:
            x[j] = x[j-1]
            j -= 1
        x[j] = tmp

    return x


data = [6, 4, 3, 7, 1, 9, 8]
result = insertion(data)
print(result)

