# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def DFS(leftNode, rightNode, level):
            if not leftNode or not rightNode :
                return
            
            if level%2==0:
                leftNode.val , rightNode.val = rightNode.val, leftNode.val

            DFS(leftNode.left, rightNode.right, level+1)
            DFS(leftNode.right, rightNode.left, level+1)

        DFS(root.left, root.right, 0)
        return root


            
        