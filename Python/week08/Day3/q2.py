import math

def plusone(a):
    n = len(a)
    a[n-1] += 1
    carry = a[n-1]/10
    a[n-1] = a[n-1] % 10

    for i in range(n-2,-1,-1):
        if (carry == 1):
           a[i] += 1
           carry = a[i]/10
           a[i] = a[i] % 10
    if (carry == 1):
      a.insert(0, 1)

aray=[4,3,2,1]
  
plusone(aray)
  
for  i in range(0, len(aray)):
     print(aray[i] ,end= " ")
  