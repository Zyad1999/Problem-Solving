def print_permutations(array):
    array.sort()
    array = tuple(array)

    # cache = {}
    def permutations_dp(array):
        # if array in cache.keys():
        #    return cache[array]

        if len(array) == 1:
            res = set()
            res.add(tuple(array, ))
            return res

        res = set()
        prev_a = None
        for i, a in enumerate(array):
            if a != prev_a:
                res1 = permutations_dp(array[:i] + array[i + 1:])
                prev_a = a
                for r in res1:
                    res.add((a,) + r)

        # cache[array] = res
        return res

    rset = permutations_dp(array)

    res = list(rset)
    res.sort()

    for r in res:
        print(' '.join([str(x) for x in r]))

n = int(input())
array = list(map(int, input().split(' ')))
print_permutations(array)
