class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p1 = p2 = m = 0
        
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1
            
        return m