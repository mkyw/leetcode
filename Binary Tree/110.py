# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1


    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1