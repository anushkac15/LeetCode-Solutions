# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def valid(left, node, right):

            if not node:
                return True

            if not (left < node.val < right):
                return False

            return valid(left, node.left, node.val) and valid(
                node.val, node.right, right
            )

        return valid(float("-inf"), root, float("inf"))
