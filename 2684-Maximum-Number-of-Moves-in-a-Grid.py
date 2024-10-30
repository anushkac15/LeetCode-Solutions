class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res =0

        def DFS(r,c,memo):
            directions = [-1,0,1]
            moves = 0

            if memo[r][c] !=-1:
                return memo[r][c]

            for dir in directions:
                newRow = r +dir
                newCol = c+1

                if newRow<row and newRow>=0 and newCol<col and newCol>=0 and grid[newRow][newCol] >grid[r][c]:
                    moves = max(moves,1+DFS(newRow,newCol,memo))

            memo[r][c] = moves
            return memo[r][c]

        memo = [[-1]*col for _ in range(row)]

        for i in range(row):
            res = max(res, DFS(i,0,memo))

        return res
        