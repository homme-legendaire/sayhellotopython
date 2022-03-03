def GuGu(num):
    result = []
    i = 1
    while i < 10:
        result.append(num*i)
        i+=1
    return result

result = GuGu(2)

print(result)