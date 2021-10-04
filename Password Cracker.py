t = int(input().strip())


def solve(passwords, loginAttempt):
    dead_end = set()

    stack = []
    stack.append(([], loginAttempt))
    while stack:
        acc, cur = stack.pop()

        if cur == "":
            return acc

        is_dead_end = True
        for password in passwords:
            if cur.startswith(password):
                cur2 = cur[len(password):]
                if cur2 in dead_end:
                    continue
                is_dead_end = False
                acc2 = acc[:]
                acc2.append(password)
                stack.append((acc2, cur2))

        if is_dead_end:
            dead_end.add(cur)


for ti in range(t):
    n = int(input().strip())
    passwords = [tmp for tmp in input().strip().split(' ')]
    loginAttempt = input().strip()
    answer = solve(passwords, loginAttempt)
    print("WRONG PASSWORD" if answer is None else " ".join(answer))