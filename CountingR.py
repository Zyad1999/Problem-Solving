x = input().lower()
n = int(input())
a = x.count('r')
c = ((n//len(x))*a)
c += x[0:(n%len(x))].count('r')
print(c)


'''
x = input().lower()
n = int(input())
c = x*(n//len(x) + 1)
b = c[0:n]
print(b.count('r'))
'''