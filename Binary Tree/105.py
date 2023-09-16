# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def print(self):
        if self.left:
            self.left.print()
        print(self.val),
        if self.right:
            self.right.print()
    
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        """
        In-order: left, root, right
        Pre-order: root, left, right
        """

        # def helper(branch, i):
        #     if len(branch) == 0:
        #         return None
        #     if len(branch) == 1:
        #         return TreeNode(branch[0], None, None)
            
        #     leftbranch = branch[:branch.index(i)]
        #     rightbranch = branch[branch.index(i) + 1:]
        #     print("left:", leftbranch)
        #     print("right:", rightbranch)

        #     if len(leftbranch) == 0:
        #         return TreeNode(branch[branch.index(i)], None, helper(rightbranch, rightbranch[len(rightbranch)//2]))
        #     elif len(rightbranch) == 0:
        #         print("branch:", branch[branch.index(i)])
        #         return TreeNode(branch[branch.index(i)], helper(leftbranch, leftbranch[len(leftbranch)//2]), None)
        #     return TreeNode(branch[branch.index(i)], helper(leftbranch, leftbranch[len(leftbranch)//2]), helper(rightbranch, rightbranch[len(rightbranch)//2]))


        if inorder:
            i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[i])
            leftbranch = inorder[:i]
            rightbranch = inorder[i + 1:]
            print("left:", leftbranch)
            print("right:", rightbranch)

            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])

            return root

t = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
# inorder = [2, 3, 1]
# preorder = [1, 2, 3]

inorder = [4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 5, 3, 6, 7]

s = Solution().buildTree(preorder, inorder)
print(s.PreorderTraversal(s))