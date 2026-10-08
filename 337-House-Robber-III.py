# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        dfs -> returns:
        - rob_node  = maximum money if we rob this node
        - skip_node = maximum money if we skip this node
        '''
        def dfs(node):
            if not node:
                return 0, 0
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # either take or skip this node:
            rob_node = node.val + left_skip + right_skip
            skip_node = max(left_skip, left_rob) + max(right_skip, right_rob) # when skip node, we can choose either to take or skip the left or right child

            return rob_node, skip_node
        
        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)