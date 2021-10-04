def look_and_say(n):
    def looksay(look):
        look = str(look)
        prev, count, say = look[0], 1, ''
        for char in look[1:]:
            if char == prev:
                count += 1
                continue
            say += str(count) + prev
            prev = char
            count = 1
        return say + str(count) + prev
    a = [1]
    for i in range(n-1):
        a.append(looksay(a[i]))
    return a[-1]

n = int(input())
answer = look_and_say(n)
print(answer)