#!/bin/python3

import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    chars = 0
    chars += 0 if any(c in numbers for c in password) else 1
    chars += 0 if any(c in lower_case for c in password) else 1
    chars += 0 if any(c in upper_case for c in password) else 1
    chars += 0 if any(c in special_characters for c in password) else 1
    return max(n + chars, 6) - n

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)