class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counter = {}
        ans = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]                
                
                if product in product_counter:
                    ans += product_counter[product]
                    product_counter[product] += 1
                else:
                    product_counter[product] = 1

        return ans * 8