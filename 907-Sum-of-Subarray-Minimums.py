class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def canEatAll(piles: List[int], mid: int, h:int)->bool:
            actualHours =0

            for banana in piles:
                actualHours += (banana+mid-1)//mid

            return actualHours<=h

        while l<r:
            mid = (l+ r)//2

            if canEatAll(piles, mid, h):
                r = mid
            else:
                l = mid+1

        return l