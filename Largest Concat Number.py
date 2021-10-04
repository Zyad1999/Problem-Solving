def largest_concat_number(numbers):
    strings = numbers
    for i in range(n):
        strings.append(input())
    c = True
    while c:
        c = False
        for i in range(n-1):
            if int(strings[i+1]+strings[i])>int(strings[i]+strings[i+1]):
                strings[i+1],strings[i] = strings[i],strings[i+1]
                c = True
    return("".join(strings))

n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())
answer = largest_concat_number(numbers)
print(answer)