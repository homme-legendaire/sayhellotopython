store = {}
while True:
    do, item = input().split()
    if do == 'i':
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    elif do == 'd':
        if item in store:
            store[item] -= 1
            if store[item] == 0:
                del store[item]
        else:
            print('no such item')
    elif do == 'u':
        if item in store:
            new = int(input())
            store[item] = new
        else:
            print('no such item')
    elif do == 'p':
        for k, v in store.items():
            print(f'{k}({v})', end=' ')
        print()
    elif do == 'a':
        print(
            f'max: {max(store, key=store.get)}({max(store.values())}), min: {min(store, key=store.get)}({min(store.values())})')
    elif do == 'q':
        break
