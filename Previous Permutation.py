def previous_permutation(permutation):
    prev = -1
    prev_i = -1
    change_i = -1
    for i in range(len(permutation)-1):
        if (permutation[i] > permutation[i+1]):
            prev = permutation[i]
            prev_i = i
        if(permutation[i+1] < prev):
            change_i = i+1
    if (prev > -1):
        temp = permutation[prev_i]
        permutation[prev_i] = permutation[change_i]
        permutation[change_i] = temp
    permutation[prev_i+1:] = sorted(permutation[prev_i+1:], reverse=True)
    return permutation if prev > -1 else [-1]

n = int(input())
permutation = list(map(int, input().split(' ')))
prev = previous_permutation(permutation)
print(' '.join(map(str, prev)))