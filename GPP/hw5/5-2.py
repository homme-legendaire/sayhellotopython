store = {}
while True:
    f, item = input().split()
    if f == 'i':
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    elif f == 'd':
        if item in store:
            store[item] -= 1
            if store[item] == 0:
                del store[item]
        else:
            print("no such item")
    elif f == 'u':
        if item in store:
            up = int(input())
            store[item] = up
            if up == 0:
                del store[item]
        else:
            print("no such item")
    elif f == 'p':
        for k, v in store.items():
            print(f"{k}({v})", end=' ')
        print()
    elif f == 'a':
        print(f'max: {max(store, key=store.get)}({max(store.values())}), min: {min(store, key=store.get)}({min(store.values())})')
    elif f == 'q':
        break
