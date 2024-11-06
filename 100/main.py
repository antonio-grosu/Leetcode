# Definirea clasei pentru un nod al arborelui
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None and q!=None:
            return False
        if p!=None and q==None:
            return False
        if p!=None and q!=None:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)


sol = Solution()



root1 = TreeNode(1)
root1.left = TreeNode(2)
root2 = TreeNode(1)
root2.left = TreeNode(2)


print(sol.isSameTree(root1,root2))