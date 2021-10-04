def pickingNumbers(a):

    maxx = 0
    num = []

    for i in range(0, len(a)):
        num.append(a.count(a[i]))

    for i in a:

        if i+1 in a and i-1 in a:
            if num[a.index(i-1)] >= num[a.index(i+1)]:
                m = a.count(i)+a.count(i-1)
                if m > maxx:
                    maxx = m
            elif num[a.index(i-1)] <= num[a.index(i+1)]:
                m = a.count(i)+a.count(i+1)
                if m > maxx:
                    maxx = m
        elif i+1 in a and i-1 not in a:
            m = a.count(i) + a.count(i + 1)
            if m > maxx:
                maxx = m
        elif i+1 not in a and i-1 in a:
            m = a.count(i) + a.count(i - 1)
            if m > maxx:
                maxx = m

    if max(num) > maxx:
        maxx = max(num)

    print(maxx)


n = int(input())
a = list(map(int, input().strip().split(' ')))
pickingNumbers(a)

'''
#def pickingNumbers(a):

#    num = []
 #   for i in range(0, len(a)):
  #      num.append(a.count(a[i]))
   # x = max(num)
  #  b = num.index(x)
  #  ma = a[b]
#    if ma - 1 in a and ma + 1 in a:
 #       if num[a.index(ma - 1)] >= num[a.index(ma + 1)]:
  #          print(a.count(ma) + a.count(ma - 1))
   #     elif num[a.index(ma - 1)] < num[a.index(ma + 1)]:
    #        print(a.count(ma) + a.count(ma + 1))
#    elif ma - 1 in a and ma + 1 not in a:
 #       print(a.count(ma) + a.count(ma - 1))
  #  elif ma - 1 not in a and ma + 1 in a:
   #     print((a.count(ma) + a.count(ma + 1)))
#    elif ma - 1 not in a and ma + 1 not in a:
 #       print(a.count(ma))

#n = int(input())
#a =list(map(int, input().strip().split(' ')))
#pickingNumbers(a)
'''