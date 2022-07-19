#b. perform the same task as given above but using one for loop only instead of 2
no_of_lines1=int(input("enter the number of rows to be printed:"))
for i in range(1,no_of_lines1+1):
  if i<=(no_of_lines1//2)+1:
    print(" "*((no_of_lines1//2)-i+1)+"*"*(2*i-1))
  else:
    print(" "*(i-(no_of_lines1//2)-1)+"*"*(2*(no_of_lines1-i)+1))