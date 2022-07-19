class Solution(object):
   def hammingWeight(self, n):
      n = str(bin(n))
      print(n)
      one_count = 0
      for i in n:
         if i == "1":
            one_count+=1
      return one_count
num = "00000000000000000000000000001011"
ob1 = Solution()
print(ob1.hammingWeight(num))