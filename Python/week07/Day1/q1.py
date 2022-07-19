def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = int(input("enter a decimal Number :  "))
     
    # Calling function
    DecimalToBinary(dec_val)