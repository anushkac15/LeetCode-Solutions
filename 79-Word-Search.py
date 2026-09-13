class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def solve(i, j, index):

            if index == len(word):
                return True

            if (
                (i < 0 or i >= len(board))
                or (j < 0 or j >= len(board[0]))
                or (board[i][j] != word[index])
            ):
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (
                solve(i + 1, j, index + 1)
                or solve(i, j + 1, index + 1)
                or solve(i - 1, j, index + 1)
                or solve(i, j - 1, index + 1)
            )

            board[i][j] = temp
            return found

        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if solve(i, j, 0):
                    return True

        return False
