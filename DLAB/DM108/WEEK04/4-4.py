i = 0
while True:
    i += 1
    if i > 100:
        break

    if i % 10 != 7:
        continue

    print(i, end=' ')
