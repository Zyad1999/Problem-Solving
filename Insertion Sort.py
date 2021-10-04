students = {}
n = int(input())
for i in range(0,n):
    x = input()
    y = int(input())
    students[x] = y

def theKey (m, students, u):
    for l in students:
        if(students[l] == m):
            if( l is u):
                continue
            else:
               return l
            break

def Sorting(a):
    p = 0
    for j in range(0, len(a)):
        c = a[p]
        for i in range(p, len(a)):
            if (a[i] > c):
                continue
            c = a[i]
            z = i
        a[j], a[z] = a[z], a[j]
        p += 1
    return a


z = 1
a = (list(students.values()))
a = Sorting(a)

for q in range(1, len(a)-1):
    if (a[1] == a[q+1]):
        z += 1

u = "nul"
for t in range(0, z):
    m = a[t+1]
    u = theKey(m, students, u)
    print(u)







