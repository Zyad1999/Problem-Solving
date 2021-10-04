N = int(input())
for z in range(0, N):
    [y1, x1] = list(map(int, input().split()))
    x1 = int(x1);
    y1 = int(y1);
    large = list();
    for i in range(0, y1):
        large.append(input())

    [y2, x2] = list(map(int, input().split()));
    small = list();
    for i in range(0, y2):
        small.append(input());

    # Work Backwards
    currentStr = small.pop()
    matches = 0;
    fail = 0;
    for i in range(0, y1):
        bigLine = large.pop();
        if (matches > 0 and fail == 1):  # if we've found a match but then the next line isn't, abort
            break;
        elif currentStr in bigLine:  # find match
            matches = matches + 1;
            if small:
                currentStr = small.pop();
            fail = 0;
        else:  # no match
            fail = 1;  # Marker to determine if from last line

    if (matches == y2):
        print("YES");
    else:
        print("NO");
