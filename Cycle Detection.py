def has_cycle(head):
    count = 0

    while head and count < 101:
        count += 1
        head = head.next

    return count > 100