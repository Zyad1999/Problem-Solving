n = int(input("Enter the Number "))
a, b, c = 0, 1, 1
print(0, end =" " )
while c < n :
    print(b, end =" ")
    a, b, c = b, a+b, c+1