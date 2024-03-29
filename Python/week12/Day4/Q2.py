import heapq
class KthLargest:

    def __init__(self, k, nums):

        self.heap = []
        self.k = k

        for i in nums:

            if len(self.heap) < k:
                heapq.heappush(self.heap,i)

            else:

                if i > self.heap[0]:
                    heapq.heappushpop(self.heap,i)
        

    def add(self, val):

        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)

        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap,val)   

        return self.heap[0]