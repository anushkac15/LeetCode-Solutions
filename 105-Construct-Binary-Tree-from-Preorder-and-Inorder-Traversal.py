# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def solve(start, end):

            if start > end:
                return None

            rootVal = preorder[idx[0]]
            idx[0] += 1

            i = pos[rootVal]
            root = TreeNode(rootVal)

            root.left = solve(start, i - 1)
            root.right = solve(i + 1, end)

            return root

        pos = {}

        for i in range(len(preorder)):
            pos[inorder[i]] = i

        idx = [0]

        return solve(0, len(preorder) - 1)
