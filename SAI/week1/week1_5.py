m,k,k1,n = input().split()
mat1 = []
mat2 = []

for i in range(int(m)):
    mat1.append(list(map(int,input().split())))
for i in range(int(k)):
    mat2.append(list(map(int,input().split())))

ans_matrix = []

for i in range(int(m)):
    sub_matrix = []
    for j in range(int(n)):
        tmp = 0
        for K in range(int(k)):
            tmp += mat1[i][K] * mat2[K][j]
        sub_matrix.append(tmp)
    ans_matrix.append(sub_matrix)
print(ans_matrix)