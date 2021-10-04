def icecreamParlor(m, a):
    # Complete this function
    d=dict()
    for i in range(len(a)):
        if( a[i] in d and d[a[i]]!=0):
            print(d[a[i]],i+1)
            break
        if(a[i]<m):
            d[m-a[i]]=i+1

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
