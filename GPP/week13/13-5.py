Grade = [
    ['C', 'B', 'A', 'C', 'D'],
    ['F', 'D', 'C', 'D', 'B'],
    ['A', 'B', 'A', 'B', 'A'],
    ['A', 'A', 'B', 'C', 'D'],
    ['B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'C', 'D', 'F'],
    ['C', 'A', 'A', 'A', 'A'],
    ['D', 'A', 'A', 'C', 'F']
]
Score = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(8):
    for j in range(3):
        if Grade[i][j] == 'A':
            Score[i] += 12.0
        elif Grade[i][j] == 'B':
            Score[i] += 9.0
        elif Grade[i][j] == 'C':
            Score[i] += 6.0
        elif Grade[i][j] == 'D':
            Score[i] += 3.0
    if Grade[i][3] == 'A':
        Score[i] += 8.0
    elif Grade[i][3] == 'B':
        Score[i] += 6.0
    elif Grade[i][3] == 'C':
        Score[i] += 4.0
    elif Grade[i][3] == 'D':
        Score[i] += 2.0
    if Grade[i][4] == 'A':
        Score[i] += 4.0
    elif Grade[i][4] == 'B':
        Score[i] += 3.0
    elif Grade[i][4] == 'C':
        Score[i] += 2.0
    elif Grade[i][4] == 'D':
        Score[i] += 1.0
    Score[i] /= 12
for i in range(8):
    print(f'{i+1} {round(Score[i],2):.2f}')
