N = int(input())
for _ in range(N):
    score = 0
    i = 0
    quiz = input()
    while i < len(quiz):
        cnt = 1
        if quiz[i] == 'O':
            while quiz[i] != 'X':
                score += cnt
                cnt += 1
                i += 1
                if i >= len(quiz):
                    break
        i += 1
    print(score)
