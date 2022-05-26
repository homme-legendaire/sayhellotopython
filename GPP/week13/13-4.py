score = []
for _ in range(8):
    score.append(int(input()))
score.sort(reverse=True)
for i in range(8):
    print(score[i])
