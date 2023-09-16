class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        n = 1

        for i in range(len(nums)):
            res[i] = n
            n *= nums[i]
        
        n = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= n
            n *= nums[i]
        
        return res
    
        answer= [1]* (len(nums))
        prefix= 1

        for i in range(len(nums)):
            answer[i] =prefix 
            prefix *= nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


    
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))