class Solution:
    def arrayRankTransform(self, arr):
        temp = sorted(set(arr))
        
        rank_map = {num: i + 1 for i, num in enumerate(temp)}
        
        ans = [rank_map[num] for num in arr]
        
        return ans

