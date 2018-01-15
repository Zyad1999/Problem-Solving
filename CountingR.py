
x = input().lower()
n = int(input())
a = x.count('r')
c = ((n//len(x))*a)
c += x[0:(n%len(x))].count('r')
print(c)
