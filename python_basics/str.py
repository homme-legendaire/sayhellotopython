head = "="
tail = """
Orange is the new black
"""

print(head*50+tail+head*50)
print(len(tail))
print(tail[2])
print(tail[-2])

slice = tail[1]+tail[2]+tail[3]+tail[4]
print(slice)

slicing = tail[1:4]
print(slicing)

slicc = tail[1:]
print(slicc)

sliced = tail[:17]
print(sliced)

print("I eat %d apples" % 3)

number = 7
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))

print("Loading... %d%%" % 97)

print("%10s" % "hi")
print("%-10sjane" % "hi")

print("%0.4f" % 3.141592)

print("I ate {0} apples".format("six"))
print("I ate {0} apples and {1} pieces of cake".format(6, "nine"))

print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

name = "이수영"
age = 22
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다. 내년이면 {age+1}살 입니다")

dic = {"name": "이수영", "age": 23}
print(f'나의 이름은 {dic["name"]}입니다. 나이는 {dic["age"]}입니다.')
