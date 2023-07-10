class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_i = 0
        index_j = 0
        for i in nums:
            for j in nums:
                if i+j == target and index_i != index_j:
                    return index_i, index_j
                index_j += 1
            index_i += 1
            index_j = 0
