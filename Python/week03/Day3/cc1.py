# a. Print the following pattern after taking in the line number as input from the user:
# for example: if input line number is 5, then print the following pattern.
# *
# ***
# *****
# ***
# *
n=int(input("enter the number of rows:"))
for i in range(1,n//2+2):
      print(" "*((n//2)-i+1)+"*"*(2*i-1))
for j in range(n//2+2,n+1):12
          print(" "*(j-(n//2)-1)+"*"*(2*(n-j)+1))
