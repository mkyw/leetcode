# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minV, maxV = min(p.val, q.val), max(p.val, q.val)

        while root:
            if minV <= root.val <= maxV:
                break
            elif root.val > maxV:
                root = root.left
            else:
                root = root.right
        
        return root