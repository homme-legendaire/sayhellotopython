a = input("a: ")
b = input("b: ")

if a == 's':
    if b == 'r':
        print('b win!')
    elif b == 'p':
        print('a win!')
    else:
        print('draw!')

elif a == 'r':
    if b == 'r':
        print('draw!')
    elif b == 'p':
        print('b win!')
    else:
        print('a win!')

else:
    if b == 'r':
        print('a win!')
    elif b == 'p':
        print('draw!')
    else:
        print('b win!')