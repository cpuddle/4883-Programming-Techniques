import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in  words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        heap = []
        for i in d:
            heapq.heappush(heap,(-1 * d[i],i))

        ans = []
        for i in range(k):
            if heap:
                x = heapq.heappop(heap)
                ans.append(x[1])
            else:
                break
        return ans
