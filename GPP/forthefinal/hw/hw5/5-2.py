store = {}
while True:
    work, item = input().split()
    if work == 'i':
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    elif work == 'd':
        if item in store:
            store[item] -= 1
            if store[item] == 0:
                del store[item]
        else:
            print('no such item')
    elif work == 'u':
        if item in store:
            mod = int(input())
            store[item] = mod
            if store[item] == 0:
                del store[item]
        else:
            print('no such item')
    elif work == 'p':
        for k, v in store.items():
            print(f'{k}({v})', end=' ')
        print()
    elif work == 'a':
        print(
            f'max: {max(store, key=store.get)}({max(store.values())}), min: {min(store, key=store.get)}({min(store.values())})')
    elif work == 'q':
        break
