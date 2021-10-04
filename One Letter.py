n = int(input())
l = []
for i in range(n):
    l.append(sorted(list(input()))[0])
print("".join(map(str,sorted(l))))