def numStonesJewels(jewels, stones):
    numStones = {}
    numJewels = 0

    for i in stones:
        if i not in numStones:
            numStones[i] = 1
        else:
            numStones[i] += 1     

    for j in jewels:
        if j in numStones:
            numJewels += numStones[j]

    return numJewels


if __name__ == "__main__":

    jewels = "aA"
    stones = "aAAbbbb"
    ans = numStonesJewels(jewels, stones)
    print(ans)
