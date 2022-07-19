class Solution:
    def longestPalindrome(self, s: str) -> int:
    	D = {}
    	for c in s:
    		if c in D:
    			D[c] += 1
    		else:
    			D[c] = 1
    	L = D.values()
    	E = len([i for i in L if i % 2 == 1])
    	return sum(L) - E + (E > 0)
