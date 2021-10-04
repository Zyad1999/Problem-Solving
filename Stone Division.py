n, m = map(int, input().split())
s = list(map(int, input().split()))

def wins(size):
    for si in s:
        if size % si == 0:
            if wins(size//si) and (si % 2 == 1):
                pass
            else:
                return True
    return False

if wins(n):
    print("First")
else:
    print("Second")