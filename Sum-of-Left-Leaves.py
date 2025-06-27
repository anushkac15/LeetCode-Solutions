# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        sum =0

        def dfs(node):
            nonlocal sum 
            if(node.left!=None):
                if(node.left.left==None and node.left.right==None):
                    sum+=node.left.val
                dfs(node.left)

            if(node.right!=None):
                dfs(node.right)

            return sum
            
        sum+=dfs(root)
        return sum
      