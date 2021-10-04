def even_steps_elimination(N):
    if N == 1:
        return 1

    else:

        if N % 2 == 1:
            return even_steps_elimination(N // 2) * 2 + 1
        else:
            return even_steps_elimination(N // 2) * 2 - 1


###
size = int(input())
answer = even_steps_elimination(size)
print(answer)