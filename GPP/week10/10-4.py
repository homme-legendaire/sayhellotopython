n = int(input())
list = []
for i in range(n):
    m = int(input())
    list.append(m)
index = int(input())
print(list[(n//2-1)+(n//2-index)])
