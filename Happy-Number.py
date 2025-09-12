class Solution:
    def isHappy(self, n: int) -> bool:

        st = set()

        while n not in st:

            if n==1:
                return True

            st.add(n)
            total=0

            for digit in str(n):
                total+= int(digit)**2

            n = total

        return False


