from heapq import heapify, heappop, heappush


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            dist = (point[0] * point[0]) + (point[1] * point[1])
            print(point[0] * point[0], point[1] * point[1])
            heappush(heap, (-dist, point))
            if len(heap) > k:
                heappop(heap)

        return [x[1] for x in heap]


c = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(c.kClosest(points, k))
