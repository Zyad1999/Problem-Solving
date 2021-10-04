#!/bin/python3

import sys

def num_great_xors(n):
    st_n = '{0:b}'.format(n)
    result = 0
    for i in range(len(st_n)):
        if st_n[-1-i] == '0':
            result += 2**i
    return result

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    print(num_great_xors(x))