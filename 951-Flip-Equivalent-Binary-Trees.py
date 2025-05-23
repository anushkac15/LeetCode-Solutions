# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True

        if root1 ==None or root2 == None:
            return False

        if root1.val!=root2.val:
            return False

        firstCheck = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        secondCheck = self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right, root2.left)
        return firstCheck or secondCheck