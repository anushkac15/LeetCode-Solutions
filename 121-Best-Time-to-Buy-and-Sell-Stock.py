class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        max_price = prices[0]
        for i in range(1,len(prices)):
            if(prices[i]>max_price):
                profit = max(profit, prices[i]-max_price)
            else:
                max_price = prices[i]
        return profit