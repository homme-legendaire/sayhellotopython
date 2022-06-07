str = ''
while True:
    alpha = input()
    if alpha == '-' or alpha == ';':
        if alpha == ';':
            break
        continue
    N = int(input())
    str += alpha*N
print(f"Result = {str}")
