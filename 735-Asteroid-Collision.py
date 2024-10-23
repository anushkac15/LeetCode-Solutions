class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            while st and a<0 and st[-1]>0:
                sum = a+st[-1]

                if sum<0:
                    st.pop()
                elif sum>0:
                    a =0
                else:
                    st.pop()
                    a=0

            if a!=0:
                st.append(a)

        s = len(st)
        res = [-1]*s
        i = s-1
        while st:
            res[i] = st[-1]
            st.pop()
            i-=1

        return res

        