list = input().split()
if list[1] == 'M':
    weight = int(list[0])/100*int(list[0])/100*22
if list[1] == 'F':
    weight = int(list[0])/100*int(list[0])/100*21
print("%.1fkg" % weight)
