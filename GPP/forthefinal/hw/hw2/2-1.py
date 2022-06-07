coding = int(input())
english = int(input())
grade = 0
if coding >= 90:
    grade += 4
elif coding >= 80:
    grade += 3
elif coding >= 60:
    grade += 2

if english >= 90:
    grade += 4
elif english >= 80:
    grade += 3
elif english >= 60:
    grade += 2

print(f"{grade/2:.2f}")
