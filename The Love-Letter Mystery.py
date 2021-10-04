x = int(input())
for i in range(x):
    s = input()
    c = 0
    if len(s) % 2 == 0:
        for i in range(int(len(s) / 2)):
            # print(abs(ord(s[i])-ord(len(S)-1-i)))
            c += abs(ord(s[i]) - ord(s[len(s) - 1 - i]))
    else:
        for i in range(int((len(s) - 1) / 2)):
            # print(abs(ord(s[i])-ord(len(s)-1-i)))
            c += abs(ord(s[i]) - ord(s[len(s) - 1 - i]))
    print(c)
