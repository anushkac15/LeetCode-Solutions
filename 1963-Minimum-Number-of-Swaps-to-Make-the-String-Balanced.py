class Solution:
    def minSwaps(self, s: str) -> int:

        open = 0

        for ch in s:
            if ch == "[":
                open += 1
            elif open > 0:
                open -= 1

        return (open + 1) // 2
