class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head.next
    fast = head.next
    
    if not head or head.next is None:
        return head
    
    while slow is not None and fast.next is not None and fast.next.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
    return slow


if __name__ == "__main__":

    head = [1,2,3,4,5]
    ans = middleNode(head)
    print(ans)