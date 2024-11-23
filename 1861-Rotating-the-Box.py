class Solution:
    def rotateTheBox(self, nums: List[List[str]]) -> List[List[str]]:
        m = len(nums)
        n = len(nums[0])
        res = [["" for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            cell = n - 1
            for j in range(n - 1, -1, -1):
                if nums[i][j] == '*':
                    cell = j - 1
                elif nums[i][j] == '#':
                    nums[i][j] = '.'
                    nums[i][cell] = '#'
                    cell -= 1
        
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = nums[i][j]

        return res
