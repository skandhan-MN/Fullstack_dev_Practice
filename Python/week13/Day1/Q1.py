def fib(N):

    res = [0, 1]
    if N == 0:
        return res[0]

    elif N==1:
        return res[1]

    for i in range(2, N+1):
        res.append(res[-1] + res[-2])  

    return res[-1]


if __name__=="__main__":

    n = 2
    ans = fib(n)
    print(ans)