class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_map = {}
        for num in nums:
            if num in cnt_map:
                cnt_map[num]+=1
            else:
                cnt_map[num]=1
            
        keys = sorted(cnt_map, key = cnt_map.get, reverse = True)
        res = keys[:k]
        return res

        