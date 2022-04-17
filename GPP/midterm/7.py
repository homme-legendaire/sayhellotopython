a1 = int(input())
a2 = int(input())
a3 = int(input())

b1 = int(input())
b2 = int(input())
b3 = int(input())

pre_a1 = int(input())
pre_a2 = int(input())
pre_a3 = int(input())

pre_b1 = int(input())
pre_b2 = int(input())
pre_b3 = int(input())

a_point = 0
a_p = 0
a_e = 0
a_n = 0

b_point = 0
b_p = 0
b_e = 0
b_n = 0

if pre_a1 == a1:
    b_point+=3
    b_p+=1
elif pre_a1 == a2 or pre_a1 == a3:
    b_point+=2
    b_e+=1
else:
    b_point-=1
    b_n+=1

if pre_a2 == a2:
    b_point+=3
    b_p+=1
elif pre_a2 == a1 or pre_a2 == a3:
    b_point+=2
    b_e+=1
else:
    b_point-=1
    b_n+=1

if pre_a3 == a3:
    b_point+=3
    b_p+=1
elif pre_a3 == a1 or pre_a3 == a1:
    b_point+=2
    b_e+=1
else:
    b_point-=1
    b_n+=1

if pre_b1 == b1:
    a_point+=3
    a_p+=1
elif pre_b1 == b2 or pre_b1 == b3:
    a_point+=2
    a_e+=1
else:
    a_point-=1
    a_n+=1

if pre_b2 == b2:
    a_point+=3
    a_p+=1
elif pre_b2 == b1 or pre_b2 == b3:
    a_point+=2
    a_e+=1
else:
    a_point-=1
    a_n+=1

if pre_b3 == b3:
    a_point+=3
    a_p+=1
elif pre_b3 == b1 or pre_b3 == b2:
    a_point+=2
    a_e+=1
else:
    a_point-=1
    a_n+=1

print(f"A's prediction about B : {a_p}p {a_e}e {a_n}n")
print(f"B's prediction about A : {b_p}p {b_e}e {b_n}n")

if a_point == b_point:
    print("Draw")
elif a_point > b_point:
    print(f"Player A is win ! {a_point-b_point} higher.")
else:
    print(f"Player B is win ! {b_point-a_point} higher.")
