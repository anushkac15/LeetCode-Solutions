class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        special = [0] * (n - 1)
        for i in range(n - 1):
            special[i] = (nums[i] % 2) != (nums[i + 1] % 2)
        
        prefix_count = [0] * n
        for i in range(1, n):
            prefix_count[i] = prefix_count[i - 1] + (0 if i > len(special) or special[i - 1] else 1)
        
        result = []
        for fromi, toi in queries:
            if toi == fromi:  
                result.append(True)
            else:
                if prefix_count[toi] - prefix_count[fromi] == 0:
                    result.append(True)
                else:
                    result.append(False)
        
        return result  