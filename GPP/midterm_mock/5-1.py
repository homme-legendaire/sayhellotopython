card1 = int(input())
card2 = int(input())
total = card1+card2
if total > 21:
    print("Lose")
elif total < 21:
    print(f"Total = {total}")
else:
    print("Black jack")
