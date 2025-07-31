class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        res = set()
        
        curr = set()

        for x in arr:

            next_ors = {x | y for y in curr}
            next_ors.add(x)
            
            res.update(next_ors)
            
            curr = next_ors
            
        return len(res)