class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag = defaultdict(list)

        for i in range(n):
            for j in range(n):
                diag[i-j].append(grid[i][j])

        for key in diag:
            if key>=0:
                diag[key].sort(reverse = True)
            else:
                diag[key].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = diag[i-j].pop(0)

        return grid
        