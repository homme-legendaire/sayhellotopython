coding = int(input())
eng = int(input())
if coding >= 90:
    coding = 4
elif coding >= 80:
    coding = 3
elif coding >= 60:
    coding = 2
else:
    coding = 0
if eng >= 90:
    eng = 4
elif eng >= 80:
    eng = 3
elif eng >= 60:
    eng = 2
else:
    eng = 0

print(f'{(coding+eng)/2:.2f}')
