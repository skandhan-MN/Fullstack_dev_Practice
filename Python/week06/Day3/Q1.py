def swap(s1, s2):
    return s2, s1

s1 = int(input("Enter your first nbumber: "))
s2 = int(input("Enter the second number: "))
s1, s2 = swap(s1, s2)
print("Values have been swaped ",s1, s2) 