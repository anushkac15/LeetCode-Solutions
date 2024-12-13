class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        memo = {}

        def dfs(n):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]
            if n % 2:
                memo[n] = 1 + dfs(3 * n + 1)
            else:
                memo[n] = 1 + dfs(n / 2)
            return memo[n]

        for n in range(hi, lo - 1, -1):
            res.append((dfs(n), n))
        heapq.heapify(res)
        while k > 1:
            heapq.heappop(res)
            k -= 1
        return res[0][1]