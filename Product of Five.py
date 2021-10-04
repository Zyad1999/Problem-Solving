def prod(arr):
    p = 1
    for i in arr:
        p *= i
    return p


def product_of_five(array):
    array.sort()

    maxP = -50 ** 5 - 1
    for i in range(6):
        left = array[:i]
        right = array[-(5 - i):] if i < 5 else []
        left += right
        maxP = max(maxP, prod(left))

    return maxP


n = int(input())
array = list(map(int, input().split(' ')))
answer = product_of_five(array)
print(answer)
