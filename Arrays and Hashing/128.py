class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        m = 0
        
        for i in numSet:
            if (i - 1) not in numSet:
                curr = i
                length = 1
                
                while (curr + 1) in numSet:
                    curr += 1
                    length += 1
                
                m = max(length, m)

        return m

nums = [7,2,-2,9,6,9,-7,2,1,-3,-1,-7,-5]
print(Solution().longestConsecutive(nums))