def get_gcd(n1, n2):
    if n1 < n2:
        smaller = n1
    else:
        smaller = n2
    for i in range(1, smaller+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd


n1 = int(input())
n2 = int(input())
print(get_gcd(n1, n2))
