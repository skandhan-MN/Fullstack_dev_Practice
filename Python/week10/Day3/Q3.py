def performXOR(x, y):
	res = 0 

	# Assuming 32-bit Integer
	for i in range(31, -1, -1):
		
		b1 = x & (1 << i)
		b2 = y & (1 << i)
		b1 = min(b1, 1)
		b2 = min(b2, 1)

		xorOP = 0
		if (b1 & b2):
			xorOP = 0
		else:
			xorOP = (b1 | b2)

		res <<= 1
		res |= xorOP
	return res

if __name__ == '__main__':

    A = 5
    B = 3
    ans = performXOR(A, B)
    print(ans)



