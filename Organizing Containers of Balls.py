cases = int (input ())
for test in range (cases):
    n = int (input ())
    sr = [0] * n
    sc = [0] * n
    for i in range (n):
        row = list (map (int, input ().split (' ')))
        for j in range (n):
            sr[i] += row[j]
            sc[j] += row[j]
    if sorted(sr) == sorted(sc):
        print ("Possible")
    else:
        print("Impossible")