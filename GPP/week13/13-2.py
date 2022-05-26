N = int(input())
SW = []
OS = []
DB = []
for i in range(N):
    a, b, c = map(int, input().split())
    SW.append(a)
    OS.append(b)
    DB.append(c)
print(f'Average(SW) = {sum(SW)//N}')
print(f'Average(OS) = {sum(OS)//N}')
print(f'Average(DB) = {sum(DB)//N}')
