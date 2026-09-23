# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        def SameTree(root, subRoot):

            if not subRoot and not root:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            left = SameTree(root.left, subRoot.left)
            right = SameTree(root.right, subRoot.right)

            return left and right

        if SameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
