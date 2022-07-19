class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if not s:
            return True
        if not t:
            return False
        for i in range(len(t)):
            if(j<len(s) and s[j]==t[i]):
                j+=1
            if(j==len(s)):
                return True
        return False