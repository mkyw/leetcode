from heapq import heapify, heappush, heappop


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxHeap = []
        for stone in stones:
            heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            x = -heappop(maxHeap)
            y = -heappop(maxHeap)
            z = abs(x - y)
            if z != 0:
                heappush(maxHeap, -z)
        return 0 if len(maxHeap) == 0 else -heappop(maxHeap)


c = Solution()
print(c.lastStoneWeight([2, 7, 4, 1, 8, 1]))
