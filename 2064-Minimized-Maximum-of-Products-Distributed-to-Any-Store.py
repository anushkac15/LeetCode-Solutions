class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def condition(k):
            return sum(ceil(q / k) for q in quantities) <= n
        
        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        