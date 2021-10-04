def superDigit(n, k):
    x = sum(map(int, list(n)))
    if k == 1:
        return super(x)
    else:
        return super(x * k)
def super(x):
    if x<10:
        print(x)
    else:
        super(sum(map(int, list(str(x)))))
if __name__ == '__main__':
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = superDigit(n, k)