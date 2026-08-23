class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def solve(i, dictSet, dp):

            if i == len(s):
                return True

            if s in dictSet:
                return True

            if dp[i]!=-1:
                return dp[i]

            for idx in range(i, len(s)):

                temp = s[i: idx+1]

                if temp in dictSet and solve(idx+1, dictSet, dp):
                    dp[i]  = True
                    return dp[i]

            dp[i] = False
            return dp[i]

        dp = [-1]*len(s)
        dictSet = set(wordDict)

        return solve(0, dictSet, dp)