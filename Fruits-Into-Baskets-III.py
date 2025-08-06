class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        block_size = int(n**0.5)+1 
        blocks = [0] * (block_size)

        curr_max = 0
        for idx, size in enumerate(baskets):
            if idx%block_size == 0:
                curr_max = size
            curr_max = max(size, curr_max)
            blocks[idx // block_size] = curr_max
        
        idx = 0
        ans = n 
        for fruit in fruits:
            found = False 
            for b in range(len(blocks)):
                
                if blocks[b] < fruit: 
                    continue

                for j in range(b*block_size, min(n, (b+1)*block_size)):
                    if baskets[j] >= fruit:
                        found = True
                        baskets[j] = -1 
                        ans -= 1
                        blocks[b] = max(
                            [baskets[i] for i in range(b*block_size, min(n, (b+1)*block_size))]
                        )
                        break
                if found: 
                    break

        return ans