class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        cnt =0

        for f in fruits:
            for b in baskets:

                if f<=b:
                    baskets.remove(b)
                    break

            else:
                cnt+=1

        return cnt
        