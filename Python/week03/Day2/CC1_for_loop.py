#given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
#and all even multiples from 2 to 20 if the number is even.
#Use both for loop and while loop.

num=input("Enter the number:")
num=int(num)
for i in range(1,21+1):
    if num%2!=0:
        print(num,"x",i,"=",num*i)
for i in range(2,20+1):
    if num%2==0:
        print(num,"x",i,"=",num*i)
