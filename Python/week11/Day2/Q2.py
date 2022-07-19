class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getDecimalValue(head):
    temp = head
    node = 0
    while (temp):
        node += 1
        temp = temp.next
    result = 0
    for i in range(node):
        result += head.val * 2 ** (node - 1 - i)
        head = head.next
    return result


if __name__ == "__main__":

    head = [1,0,1]
    ans = getDecimalValue(head)
    print(ans)