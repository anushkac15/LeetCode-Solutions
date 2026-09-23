# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        def solve(node, level, res):

            if not node:
                return None

            if len(res) == level:
                res.append(node.val)

            right = solve(node.right, level + 1, res)
            left = solve(node.left, level + 1, res)

            return res

        res = []
        solve(root, 0, res)
        return res
