def myAtoiRecursive(string, num):
    if len(string) == 1:
        return int(string) + (num * 10)
    num = int(string[0:1]) + (num * 10)
    return myAtoiRecursive(string[1:], num)
string = "1234"
print(myAtoiRecursive(string, 0))