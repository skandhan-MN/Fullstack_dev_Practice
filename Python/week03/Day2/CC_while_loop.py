#given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
#and all even multiples from 2 to 20 if the number is even.
#Use both for loop and while loop.

num=input("Enter the number:")
num=int(num)
i=1
while i<=21:
    if num%2!=0:
        print(num,"x",i,"=",num*i)
        i=i+1
    i=2
    while i<=20:
        if num%2==0:
            print(num,"x",i,"=",num*i)
        i=i+2



