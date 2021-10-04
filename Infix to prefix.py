class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]


def reverse(expression):
    num = Stack()
    RevInfix = []
    for i in expression[::-1]:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            num.push(i)
        elif i == " ":
            continue
        elif i in ["+", "-", "*", "/", "^", "(", ")"]:

            while not num.is_empty():
                RevInfix.append(num.pop())
            if i == "(":
                RevInfix.append(")")
            elif i == ")":
                RevInfix.append("(")
            else:
                RevInfix.append(i)
    while not num.is_empty():
        RevInfix.append(num.pop())
    return RevInfix

def reverse2(expression):
    num = Stack()
    RevInfix = []
    for i in expression[::-1]:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            num.push(i)
        elif i == " ":
            while not num.is_empty():
                RevInfix.append(num.pop())
            RevInfix.append(' ')
        elif i in ["+", "-", "*", "/", "^"]:
                RevInfix.append(i)
    while not num.is_empty():
        RevInfix.append(num.pop())
    return RevInfix

def RevInfixToPrefix(infix):
    i = 0
    s = Stack()
    postfix = []
    higher_precedence = {"(": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}

    while i < len(infix):
        if infix[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            while i < len(infix) and infix[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                postfix.append(infix[i])
                i += 1

            postfix.append(' ')
        elif infix[i] == '(':
            s.push(infix[i])
            i += 1
        elif infix[i] == ')':
            while s.top() != '(':
                postfix.append(s.pop())
                postfix.append(" ")
            s.pop()
            i += 1
        elif infix[i] in ['+', '-', '*', '/', '^']:
            while not s.is_empty() and higher_precedence[s.top()] > higher_precedence[infix[i]]:
                postfix.append(s.pop())
                postfix.append(' ')

            s.push(infix[i])
            i += 1
        else:
            i += 1

    while not s.is_empty():
        postfix.append(s.pop())
        postfix.append(' ')
        i += 1

    return postfix

def calculate(prefix):

    calc = Stack()
    i = len(prefix)-1
    while i >= 0:
        j = i-1
        k = i
        if prefix[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            while j > 0 and prefix[j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                j -= 1
                i -= 1
            calc.push(int("".join(prefix[j+1:k+1])))
            i -= 1
        elif prefix[i] in ['+', '-', '*', '/', '^']:
            if prefix[i] == "+":
                x = calc.pop() + calc.pop()
                calc.push(x)
                i -= 1
            elif prefix[i] == "-":
                x = calc.pop() - calc.pop()
                calc.push(x)
                i -= 1
            elif prefix[i] == "*":
                x = calc.pop() * calc.pop()
                calc.push(x)
                i -= 1
            elif prefix[i] == "/":
                x = calc.pop() / calc.pop()
                calc.push(x)
                i -= 1
            elif prefix[i] == "^":
                x = calc.pop() ** calc.pop()
                calc.push(x)
                i -= 1
        else:
            i -= 1
    return calc.top()

infix = input().strip()
ReversedInfix = reverse(infix)
postfix = RevInfixToPrefix(ReversedInfix)
Prefix = reverse2(postfix)
print("Infix : ", infix)
print("Prefix: ", "".join(Prefix))
print(calculate(Prefix))
