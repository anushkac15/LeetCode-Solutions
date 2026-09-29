class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ")":
            return False

        def solve(i, j, bal):
            if grid[i][j] == "(":
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                return False

            if i == m - 1 and j == n - 1:
                return bal == 0

            if dp[i][j][bal] != -1:
                return dp[i][j][bal]

            right = down = False

            if i + 1 < m:
                down = solve(i + 1, j, bal)
            if j + 1 < n:
                right = solve(i, j + 1, bal)

            dp[i][j][bal] = right or down
            return dp[i][j][bal]

        dp = [[[-1] * (m + n) for _ in range(n)] for _ in range(m)]
        return solve(0, 0, 0)
