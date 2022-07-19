n=input("enterin number of lines:")
n=int(n)
for line_number in range(1,n+1):
    if line_number <= (n//2+n%2):
        print("*" *line_number)
    else:
        print("*" *(n-line_number+1))
