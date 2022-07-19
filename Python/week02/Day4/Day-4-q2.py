#Write a program that takes in 2 numbers and returns true if they are divisible by each other. False otherwise.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c= not(bool(a%b) and bool(b%a))
print(c)
