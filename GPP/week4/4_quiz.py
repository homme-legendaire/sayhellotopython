str = ''
while True:
    ch = input()
    if ch == ';':
        break
    elif ch == '-':
        continue
    N = int(input())
    for i in range(N):
        str += ch
print(f"Result = {str}")
