def baseballGame(ops):

    stack = []
    increment = 0

    for op in ops:

        if op == "C":
            increment -= stack.pop()
        elif op == 'D':
            stack.append(2*stack[-1])
            increment += stack[-1]
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
            increment += stack[-1]
        else:
            stack.append(int(op))
            increment += stack[-1]

    return increment


if __name__ == "__main__":

    ops = ["5","2","C","D","+"]
    output = baseballGame(ops)
    print(output)
