# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1+ max((self.maxDepth(root.left) , self.maxDepth(root.right)))
    


root = TreeNode(3)
root.right = TreeNode(20)
root.left = None




sol = Solution()
print(sol.maxDepth(root))