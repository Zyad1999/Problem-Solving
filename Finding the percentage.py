n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
a = list(student_marks[query_name])
average = float(((a[0]+a[1]+a[2])/3))
print("{:.2f}".format(average))