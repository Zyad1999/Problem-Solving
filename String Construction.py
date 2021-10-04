#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p = ""
    cost = 0
    for j in range(len(s)):
        if s[j] not in s[:j]:
            cost += 1
        p += s[j]
    print(cost)