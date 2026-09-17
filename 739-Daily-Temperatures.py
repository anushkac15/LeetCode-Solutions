class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):

            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()

            if st:
                res[i] = st[-1] - i

            st.append(i)

        return res
