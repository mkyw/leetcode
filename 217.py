class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        e = list()
        for i in nums:
            if i not in e:
                e.append(i)
            else:
                return True

        return False
