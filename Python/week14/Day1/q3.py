class Solution:
    def findCenter(self, edges) -> int:
        dic = {}
        for i in edges:
            dic[i[0]] = dic.get(i[0],0) + 1
            dic[i[1]] = dic.get(i[1],0) + 1
        n = len(dic.keys())
        for i in dic.keys():
            if dic[i] == n-1:
                return i
