dic1 = {}
dic2 = {}
dic3 = {}
listt = []
while True:
    gye, cha = map(int, input().split())
    dic1[cha] = gye
    if cha == 0:
        break
while True:
    gye, cha = map(int, input().split())
    dic2[cha] = gye
    if cha == 0:
        break
for i in dic1:
    for j in dic2:
        if i == j:
            dic3[i] = dic1[i]+dic2[j]
            listt.append(i)
for i in dic1:
    if i in listt:
        continue
    dic3[i] = dic1[i]
for i in dic2:
    if i in listt:
        continue
    dic3[i] = dic2[i]
dic4 = dict(reversed(sorted(dic3.items())))
list2 = list(dic4)
list3 = list(dic4.values())

string = f'{list3[0]}x^{list2[0]}'

for i, (k, v) in enumerate(zip(list2, list3)):
    if i == 0:
        continue
    if v == 0:
        continue
    if k == 0:
        string += f' + {v}'
        continue
    string += f' + {v}x^{k}'
print(string)
