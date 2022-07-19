#Take a number as input from the user, print its multiple of 2, 4, 6, 8, 10 if it is an odd number, if it is an even number then print its multiple of 1, 3, 5, 7 and 9.
num=int(input("Enter a Number:"))
mod=num%2
if mod>0:
    print("The given input is an odd number when it is multiplied by 2 you get ", num*2)
    print("The given input is an odd number when it is multiplied by 4 you get", num*4)
    print("The given input is an odd number when it is multiplied by 6 you get", num*6)
    print("The given input is an odd number when it is multiplied by 8 you get", num*8)
    print("The given input is an odd number when it is multiplied by 10 you get", num*10)
   
else:
    print("The given input is an Even number when it is multiplied by 1 you get ", num*1)
    print("The given input is an Even number when it is multiplied by 3 you get ", num*3)
    print("The given input is an Even number when it is multiplied by 5 you get ", num*5)
    print("The given input is an Even number when it is multiplied by 7 you get ", num*7)
    print("The given input is an Even number when it is multiplied by 9 you get ", num*9)

    
   
