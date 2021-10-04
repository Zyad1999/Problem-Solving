from collections import defaultdict


def pair_strange_sort(array):
    data = defaultdict(list)
    for val in array:
        data[val[0]].append(val[1])

    ans = []
    for key, value in sorted(data.items()):
        data2 = defaultdict(int)
        for second in value:
            data2[second] += 1

        while len(data2) > 0:
            for i in sorted(data2.keys()):
                ans.append([key, i])
                data2[i] -= 1
                if data2[i] == 0:
                    data2.pop(i)
    return ans

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split(' '))))
sorted_array = pair_strange_sort(array)
for element in sorted_array:
    print(str(element[0]) + " " +  str(element[1]))