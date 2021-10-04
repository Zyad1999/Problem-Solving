def find_start_end(field, n, m):
    for row_idx in range(n):
        for col_idx in range(m):
            if field[row_idx][col_idx] == 'M':
                start = (row_idx, col_idx)
            if field[row_idx][col_idx] == '*':
                end = (row_idx, col_idx)
    return (start, end)


def move(start, end, field, n, m, parent_nodes, child_nodes):
    children = list()
    for modifier in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        row = start[0] + modifier[0]
        col = start[1] + modifier[1]
        if row < n and row >= 0 and col < m and col >= 0:
            if (field[row][col] == '.' or field[row][col] == '*') and (row, col) not in child_nodes:
                children.append((row, col))
                child_nodes[(row, col)] = start
    parent_nodes[start] = children
    if end not in children:
        for start in children:
            move(start, end, field, n, m, parent_nodes, child_nodes)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    field = list()
    for _ in range(n):
        field.append([x for x in input()])
    k = int(input())
    start, end = find_start_end(field, n, m)
    parent_nodes = dict()
    child_nodes = dict()
    move(start, end, field, n, m, parent_nodes, child_nodes)
    count_cross = 0
    while end != start:
        end = child_nodes[end]
        if len(parent_nodes[end]) > 1:
            count_cross += 1
    if count_cross == k:
        print('Impressed')
    else:
        print('Oops!')