class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:

#     def is_subtree(self, root: TreeNode, sub_root: TreeNode) -> bool:

#         def is_same_tree(tree1, tree2):

#             if tree1 is None and tree2 is None:
#                 return True

#             if tree1 is None or tree2 is None:
#                 return False
            
#             return (tree1.val == tree2.val and
#                     is_same_tree(tree1.left, tree2.left) and
#                     is_same_tree(tree1.right, tree2.right))
        
#         if root is None:
#             return False

#         return (is_same_tree(root, sub_root) or
#                 self.is_subtree(root.left, sub_root) or
#                 self.is_subtree(root.right, sub_root))


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def isSameTree(tree1,tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None :
                return False
            return (tree1.val == tree2.val and isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right))
        
        if root is None:
            return False
        return (isSameTree(root, subRoot) or self.isSubtree(root.left , subRoot) or self.isSubtree(root.right, subRoot))


        
root1 = TreeNode(3)
root1.left =  TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(2)

sol = Solution()
print(sol.isSubtree(root1,root2))
