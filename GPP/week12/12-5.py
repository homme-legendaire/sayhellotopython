user_info = {'name': 'David', 'age': 21, 'address': 'Gwangjin-gu, Seoul'}
N = int(input())
for i in range(N):
    cnt = 0
    print(f'Edit #{i+1}')
    key = input()
    value = input()
    for j in user_info:
        if key == j:
            user_info[j] = value
            cnt = 1
            break
    if cnt == 0:
        user_info[key] = value
print('USER INFO')
for k, v in user_info.items():
    print(f'{k} : {v}')
