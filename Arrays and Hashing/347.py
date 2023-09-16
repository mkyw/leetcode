import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] = my_dict[i] + 1
            else:
                my_dict[i] = 1
        
        print(my_dict)

        my_dict = sorted(my_dict, key=my_dict.get, reverse=True)

        result = [key for key in my_dict][:k]

        return result



nums = [1,1,1,2,2,3]
k = 2

print(Solution().topKFrequent(nums, k))