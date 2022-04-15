card1 = int(input())
card2 = int(input())
total = card1+card2
while total < 21:
    go = int(input())
    if go == 1:
        total += int(input())
    else:
        break
if total > 21:
    print("Lose")
elif total < 21:
    print(f"Total = {total}")
else:
    print(f"Black jack")
