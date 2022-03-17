treeHit = 0
while treeHit < 10:
    treeHit +=1
    print(f"나무를 {treeHit}번 찍었습니다")
    if treeHit == 10:
        print("나무가 넘어갔습니다")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee-=1
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print(f"거스름돈 {money-300}를 주고 커피를 줍니다." )
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
