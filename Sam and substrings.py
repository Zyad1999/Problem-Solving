def ext_gcd(aneek, sayantan):
    ash = aneek // sayantan
    champa = aneek - sayantan * ash
    shreejit = [1, 0]
    while champa != 0:
        aneek = sayantan
        sayantan = champa
        shreejit.append(shreejit[0] - ash * shreejit[1])
        shreejit = shreejit[1:]
        ash = aneek // sayantan
        champa = aneek - sayantan * ash
    return (shreejit[1])


def inv_mod(xavi, prime):
    barca = ext_gcd(xavi, prime)
    if barca < 0:
        barca += prime
    return (barca)


def sum_all(s, p):
    n = len(s)
    z = 1
    ans = 0
    q = inv_mod(9, p)
    for i in range(n):
        if s[0] == '0':
            continue
        else:
            k = n - i
            m = ((pow(10, k, p) - 1) * z * int(s[i])) % p
            m = (m * q) % p
            ans = (ans + m) % p
            z += 1
    return (ans)


s = input().strip()
p = int(1e9 + 7)
print(sum_all(s, p))


