def reverseString(str):
    
    if not str or len(str) <= 1:
        return str
    
    left = 0
    right = len(str)-1
    
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return str


if __name__ == "__main__":

    s = ["h","e","l","l","o"]
    res = reverseString(s)
    print(res)




