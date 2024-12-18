class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        nse = [-1] * n
        st = []
        
        st.append(n - 1)
        for i in range(n - 2, -1, -1):
            while st and prices[st[-1]] > prices[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        
        ans = [0] * n
        for i in range(n):
            if nse[i] == -1:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - prices[nse[i]]
        
        return ans