for case in range(int(input())):
    N = int(input())
    arr = list(map(int,input().rstrip().split()))

    def red(target):
        ans = 0
        for i in arr:
            d = i - target
            if d >= 5:
                ans += d//5
                d %= 5
            if d >= 2:
                ans += d//2
                d %= 2
            ans += d
        return ans

    mi = min(arr)
    print(min(red(mi),red(mi-1),red(mi-2)))