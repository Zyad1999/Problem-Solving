mod = 10**9 + 7

def pal(s):
    states1 = [0]*26
    states2 = [[0]*26 for i in range(26)]
    states3 = [[0]*26 for i in range(26)]
    complete = 0
    j = 0
    for c in s:
        j += 1
        c = ord(c)-97
        complete = (complete + sum(states3[c])) % mod
        for i in range(26):
            states3[i][c] = (states3[i][c] + states2[i][c]) % mod
        for i in range(26):
            states2[i][c] = (states2[i][c] + states1[i]) % mod
        states1[c] = (states1[c] + 1) % mod
    return complete

print(pal(input()) % mod)