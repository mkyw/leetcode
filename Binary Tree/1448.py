# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good = 0
        
        def helper(root, pMaxVal):
            if not root:
                return 0
            if root.val >= pMaxVal:
                pMaxVal = root.val
                return 1 + helper(root.left, pMaxVal) + helper(root.right, pMaxVal)
            return helper(root.left, pMaxVal) + helper(root.right, pMaxVal)

        return helper(root, root.val)
    
x = TreeNode(3, TreeNode(1, TreeNode(3, None, None), None), TreeNode(4, TreeNode(1, None, None), TreeNode(5, None, None)))
s = Solution()

print(s.goodNodes(x))