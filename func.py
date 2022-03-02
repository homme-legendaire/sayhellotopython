def add(a,b):
    return a+b
print(add(3,5))
c = add(4,8)
print(c)

def say():
    return "Hi"
a = say()
print(a)

def add(a,b):
    print(f"{a}와 {b}의 합은 {a+b}입니다.")
add(5,9)
a = add(5,9)
print(a)

def say():
    print("Hi")
say()

def add(a,b):
    return a+b
result = add(b=3,a=4)
print(result)

def add_many(*args):
    result=0
    for i in args:
        result+=i
    return result
print(add_many(1,2,3))
print(add_many(1,2,3,4,5,6,7,8,9,10))

def add_mul(choice, *args): 
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result
print(add_mul("add", 1,2,3,4,5))
print(add_mul("mul", 1,2,3,4,5))

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

def say_nick(nick): 
    if nick == "바보": 
        return 
    print(f"나의 별명은 {nick} 입니다." )
say_nick("짱구")
say_nick("바보")

def say_myself(name, old, man=True): 
    print(f"나의 이름은 {name} 입니다.") 
    print(f"나이는 {old}살입니다." ) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself("이수영", 22)
say_myself("이수영", 22, True)

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

add = lambda a,b:a+b
print(add(3,7))
