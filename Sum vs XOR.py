n = int(input().strip())
print(1 if n == 0 else 1 << (bin(n)[2:].count('0')))