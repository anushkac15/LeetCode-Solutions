# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_so_far):
            if not root:
                return 0

            cnt = 1 if root.val >= max_so_far else 0

            max_so_far = max(max_so_far, root.val)

            cnt += dfs(root.left, max_so_far)
            cnt += dfs(root.right, max_so_far)

            return cnt

        return dfs(root, root.val)
