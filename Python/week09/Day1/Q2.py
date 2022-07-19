def sumDigits(no): 
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))  
    
n = 12345
print(sumDigits(n))