import sys

t = int(sys.stdin.readline().strip())
for tests in range(t):
    a,b = [int(x) for x in sys.stdin.readline().split()]
    msb_a = 0
    msb_b = 0
    mask = 1 << 31
    a_test = True
    b_test = True
    if a == 0:
        msb_a = 0
        a_test = False
    if b == 0:
        msb_b = 0
        b_test = False
    while a_test or b_test:
        if mask & a != 0:
            msb_a = mask
            a_test = False
        if mask & b != 0:
            msb_b = mask
            b_test = False
        mask = mask >> 1
    if msb_b > msb_a:
        print(0)
    else:
        if a % 2 == 0:
            print(a)
        else:
            print(msb_a)