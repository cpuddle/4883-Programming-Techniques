from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=PriorityQueue()
        for val in nums:
            maxheap.put((-val,val))
        for i in range(1,k):
            maxheap.get()
        return maxheap.get()[1]
