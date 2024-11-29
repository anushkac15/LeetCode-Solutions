class Solution:
    def balancedStringSplit(self, s: str) -> int:

        cnt =0
        bal =0
        
        for i in range(len(s)):
            if s[i] =='L':
                bal+=1
            if s[i] == 'R':
                bal -=1
            
            if bal ==0:
                cnt+=1

        return cnt
      