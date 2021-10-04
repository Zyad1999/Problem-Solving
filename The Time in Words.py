h = int(input())
m = int(input())
from n2w import convert

if m == 0 :
    print(convert(h), "o' clock")
elif m == 30:
    print("half past", convert(h))
elif m > 30:
    if m == 45:
        print("quarter to", convert(h+1))
    else:
        print(convert(60-m), 'minutes to', convert(h+1))
elif m < 30:
    if m == 15:
        print("quarter past", convert(h))
    else:
        print(convert(m), 'minutes past', convert(h))