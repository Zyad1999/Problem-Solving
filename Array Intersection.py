def array_intersection(a1, a2):
    a1.sort()
    a2.sort()
    a3 = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            a3.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    print(len(a3))
    return a3

n, m = map(int, input().split(' '))
a1 = list(map(int, input().split(' ')))
a2 = list(map(int, input().split(' ')))
intersection = array_intersection(a1, a2)
print(' '.join(map(str, intersection)))