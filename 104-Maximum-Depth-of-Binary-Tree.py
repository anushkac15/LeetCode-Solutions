# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def solve(root, cnt):
            if not root:
                return cnt

            cnt += 1

            left = solve(root.left, cnt)
            right = solve(root.right, cnt)

            return max(left, right)

        return solve(root, 0)
