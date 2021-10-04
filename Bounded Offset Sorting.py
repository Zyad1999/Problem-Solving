def bounded_offset_sorting(array, m):
    if m == 0:
        return array
    for i in range(0, len(array), m):
        array[i:i + 2*m] = sorted(array[i:i + 2*m])
    array[i:] = sorted(array[i:])
    return array

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
sorted_array = bounded_offset_sorting(array, n)
print(' '.join(map(str, sorted_array)))