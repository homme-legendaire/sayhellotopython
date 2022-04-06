i = 0
while True:
    if i % 10 != 7:
        i += 1
        continue

    if i > 100:
        break

    print(i, end=' ')
    i += 1
