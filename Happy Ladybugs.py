from collections import Counter

def unhappy(b):
    c = 1
    for i in range(0, len(b) - 1):
        if b[i + 1] == b[i]:
            c += 1
        else:
            if c <= 1:
                return True
    return False

Q = int(input().strip())
for a in range(Q):
    n = int(input().strip())
    b = input().strip()
    c = Counter(b)
    if any(1 for k, v in c.items() if v == 1 and k != '_'):
        print('NO')
    elif c.get('_', 0) == 0 and unhappy(b):
        print('NO')
    else:
        print('YES')
