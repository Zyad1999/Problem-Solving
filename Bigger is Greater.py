for _ in range(int(input())):
    x = input()
    h = False
    for i in range(len(x)-1)[::-1]:
        if x[i] < x[i+1]:
            for j in range(i+1,len(x))[::-1]:
                if x[i] < x[j]:
                    l = list(x)
                    l[i],l[j]=l[j],l[i]
                    print("".join(l[:i+1]+l[i+1:][::-1]))
                    h = True
                if h == True:
                    break
        if h == True:
            break
    if h == False:
        print("no answer")