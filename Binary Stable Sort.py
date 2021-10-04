def binary_stable_sort_cheatin(array):
    array.sort(key = lambda x: (x[1]))

def binary_stable_sort(array):
    n = len(array)
    w = 1
    while w < n:
        i = 0
        while i + w < n:
            b = -1
            l0, l1 = 0, 0
            for j in range(i, min(i + 2*w, n)):
                if (j < i + w) and (array[j][1] == 'R') and (b == -1):
                    b = j
                    l1 = i + w - j
                elif (j >= i + w) and (array[j][1] == 'B'):
                    l0 = j - (i + w) + 1
            i += 2 * w
            if (l1 > 0 and l0 > 0):
                array[b:b+l1+l0] = reversed(array[b:b+l1+l0])
                array[b:b+l0] = reversed(array[b:b+l0])
                array[b+l0:b+l0+l1] = reversed(array[b+l0:b+l0+l1])

        w *= 2

###
n = int(input())
array = []
for i in range(n):
    name, value = input().split(' ')
    array.append((name, value))
binary_stable_sort(array)
for element in array:
    print(element[0])