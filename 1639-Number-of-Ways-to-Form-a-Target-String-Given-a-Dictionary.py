class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = int(1e9 + 7) 
        
        k = len(words[0])
        m = len(target)
        
        freq = [[0] * k for _ in range(26)]
        
        for col in range(k):
            for word in words:
                freq[ord(word[col]) - ord('a')][col] += 1
        
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        
        dp[0][0] = 1
        
        for i in range(m + 1): 
            for j in range(k + 1):  
                if j < k:
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
                
                if i < m and j < k:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + freq[ord(target[i]) - ord('a')][j] * dp[i][j]) % MOD
        
        return dp[m][k]
