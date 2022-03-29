A, B, V = map(int, input().split())
S = int((V-B)/(A-B))
if ((V-A) % (A-B) == 0):
    print(S)
else:
    print(S+1)
