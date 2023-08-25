# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        queue = [root]
        level = []
        while queue:
            if not root:
                return []
            for i in range(len(queue)):
                t = queue.pop(0)
                level.append(t.val)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
            traversal.append(level)
            level = []
            
        
        return traversal