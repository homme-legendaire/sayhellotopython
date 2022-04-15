card = int(input())
while card < 17:
    card +=int(input())
if card > 21:
    print("Lose")
elif card < 21:
    print(f"Total = {card}")
else:
    print("Black jack")
        
