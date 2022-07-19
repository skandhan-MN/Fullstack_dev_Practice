def checkPalindrome(str):
   
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

st = "malayalam"
if(checkPalindrome(st) == True):
    print("it is a palindrome")
else:
    print("It is not a palindrome")