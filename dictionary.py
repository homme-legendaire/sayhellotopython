dic = {'name':'이수영', 'phone':'01028364252', 'birth':'0115'}
print(dic)

dic['address']='Seoul,Korea'
print(dic)

del dic['phone']
print(dic)

print(dic['birth'])

print(dic.keys())

for k in dic.keys():
    print(k)

print(dic.values())

print(dic.items())

#dic.clear() // 지우기
#print(dic)

print(dic.get('name'))
print(dic.get('address'))

print('name' in dic)