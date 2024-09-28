class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        beautiful_count = 0
        
        for start in range(len(s)):
            cntv = 0
            cntc = 0
            
            for end in range(start, len(s)):
                if s[end] in vowels:
                    cntv += 1
                else:
                    cntc += 1
                
                if cntv == cntc and (cntc * cntv) % k == 0:
                    beautiful_count += 1
        
        return beautiful_count
