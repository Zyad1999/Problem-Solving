n, k = map(int, input().split())
contestsSI = []
contestsS = []
contestsI = []

for i in range(0, n):
    x, y = map(int, input().split())
    if y == 1:
        contestsSI.append(x)
    else:
        contestsS.append(x)
sbw = 0
if len(contestsSI) > k:
    sbw = len(contestsSI)-k
contestsSI = sorted(contestsSI)
loseluck = contestsSI[0:sbw]
contestsSI = contestsSI[sbw:]

luck = sum(contestsSI)+sum(contestsS)-sum(loseluck)

print(luck)

'''
n, k = map(int, input().split())
contests = []
important = 0
impo = []
for contests_i in range(n):
    contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
    if contests_t[1] == 1:
        important += 1
        impo.append(contests_i)
    contests.append(contests_t)

sbw = important - k

won = 0
e = 0
el = []
while won < sbw:
    min = 1000000000
    for i in impo:
        if contests[i][0] < min and i not in el:
            min = contests[i][0]
            e = i
    won += 1
    el.append(e)


luck = 0
for i in range(0, len(contests)):
    if i not in el:
        luck += contests[i][0]
for i in el:
    luck -= contests[i][0]

print(luck)
'''