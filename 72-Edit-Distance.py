class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp, dpPrev = [-1] * (n+1), [-1] * (n+1)

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[j] = j  
                elif j == 0:
                    dp[j] = i 
                elif s1[i-1] == s2[j-1]:
                    dp[j] = dpPrev[j-1]
                else:
                    dp[j] = min(dpPrev[j], dp[j-1], dpPrev[j-1]) + 1
            dp, dpPrev = dpPrev, dp
            
        return dpPrev[n]