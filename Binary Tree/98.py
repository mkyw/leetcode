# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def helper(root, min, max):
            if not root:
                return True
            if not min <= root.val <= max:
                return False
            return helper(root.left, min, root.val) and helper(root.right, root.val, max)
        
        # def helper(root, min, max):
        #     if not root:
        #         return True
        #     if root.val <= min or root.val >= max:
        #         return False
        #     return helper(root.left, min, root.val) and helper(root.right, root.val, max)
        
        return helper(root.left, float('-inf'), root.val) and helper(root.right, root.val, float('inf'))
    
t = TreeNode(3, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)), TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)))
print(Solution().isValidBST(t))
