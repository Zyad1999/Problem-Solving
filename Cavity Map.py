n = int(input())

a = []
b = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in map(int, list(input()))]
    b.append(a_t)

for i in range(1,n-1):
    for j in range(1,n-1):
        if ( b[i][j]> b[i - 1][j] and b[i][j] > b[i][j - 1] and b[i][j] > b[i + 1][j] and b[i][j] > b[i][j + 1]):
            a.append(i)
            a.append(j)

k = 0
while (k < len(a)):
    b[a[k]][a[k+1]] = 'X'
    k += 2

for d in range(0,n):
    for g in range(0,n):
        if (g == n-1):
            print(b[d][g])
        else:
            print(b[d][g], end="")





#!/bin/python3

import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n1=len(grid)
    n2=len(grid[0])
    for i in range(1,n1-1):
        for k in range(1,n2-1):
            temp=int(grid[i][k])
            if temp>int(grid[i][k+1]) and temp>int(grid[i][k-1]) and temp>int(grid[i+1][k])and temp>int(grid[i-1][k]) :
                grid[i]=grid[i].replace(grid[i][k],'x')
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
