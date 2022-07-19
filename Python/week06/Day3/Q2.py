import math
def isPerfectSquare(x):
    if(x >= 0):
        sr = math.sqrt(x)
        return (int(sr*sr) == x)
    return False

x = int(input("Enter a number to check if the number is perfect square root or not : " ))
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")