info = input()
height = int(info[:3])
sex = info[4]
if sex == 'M':
    avg = height*height*22/10000
else:
    avg = height*height*21/10000
print(f'{avg:.1f}kg')
