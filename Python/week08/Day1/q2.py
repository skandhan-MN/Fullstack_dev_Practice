def get_digit(num):
    if num < 10:
        print(num)
    else:
        get_digit(num // 10)
        print(num % 10)
num=1234567
print(get_digit(num))   