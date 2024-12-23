
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        ans = 0
        d = {}

        while q:

            level = []

            for i in range(len(q)):

                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)

            final = sorted(level)

            for i in range(len(level)):
                d[final[i]] = i

            for i in range(len(level)):
                if i == d[level[i]]: continue

                while i != d[level[i]]:
                    temp = level[d[level[i]]]
                    level[d[level[i]]] = level[i]
                    level[i] = temp
                    ans+=1
        return ans