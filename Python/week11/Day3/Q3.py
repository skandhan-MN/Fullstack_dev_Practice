# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeInBetween(self, list1, a, b, list2):

        start = None
        end = list1
        for i in range(b):

            if i == a - 1:
                start = end
            end = end.next
        start.next = list2

        while list2.next:

            list2 = list2.next
        list2.next = end.next
        end.next = None

        return list1


if __name__ == "__main__" :

    list1 = [0,1,2,3,4,5] 
    a = 3
    b = 4
    list2 = [1000000,1000001,1000002]
    # Solution(list1, a, b, list2)    
