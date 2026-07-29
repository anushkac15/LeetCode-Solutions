class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        m = len(s) >> 1
        freq = Counter(s[:m])

        ways = factorial(m)      
        for v in freq.values():
            ways //= factorial(v)

        if k > ways: return ""

        half = ""
        for i in range(m):       
            for c in ascii_lowercase:
                if not freq[c]: continue

                t = ways * freq[c] // (m - i) 
                if k <= t: 
                    half += c    
                    freq[c] -= 1
                    ways = t  
                    break
                k -= t           

        mid = s[m] if len(s) & 1 else ""
        return half + mid + half[::-1]