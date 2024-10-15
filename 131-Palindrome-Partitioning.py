class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def palindrome(s:str)->bool:
            return s == s[::-1]

        def solve(start: int, temp :List[str]):
            if start==len(s):
                res.append(temp.copy())
                return

            for i in range(start+1, len(s)+1):
                sub = s[start:i]
                if palindrome(sub):
                    temp.append(sub)
                    solve(i, temp)
                    temp.pop()
        temp =[]
        solve(0,temp)
        return res
        