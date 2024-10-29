class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longestStreak = 0
        currentStreak = 1  

        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:  
                currentStreak += 1
            else:
                longestStreak = max(longestStreak, currentStreak)
                currentStreak = 1  

        longestStreak = max(longestStreak, currentStreak)  
        return longestStreak