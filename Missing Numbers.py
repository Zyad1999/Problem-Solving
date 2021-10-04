def missingNumbers(arr, brr):
    l = [0] * (max(arr + brr) + 1)
    for i in arr:
        l[i] += 1
    for u in brr:
        l[u] -= 1
    result = [x for x in range(len(l)) if l[x] != 0]
    return result


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(" ".join(map(str, result)))