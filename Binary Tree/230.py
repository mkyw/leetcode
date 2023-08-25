# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        
        list = []

        def helper (root):
            if root.left:
                helper(root.left)
            list.append(root.val)
            if root.right:
                helper(root.right)
        
        helper(root)
        return(list[k-1])
    
t = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), TreeNode(4, None, None)), TreeNode(6, None, None))
print(Solution().kthSmallest(t, 3))