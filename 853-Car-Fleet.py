class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        cars = sorted(zip(position, speed))
        st = []

        for pos, speed in cars:

            time = (target - pos) / speed

            while st and st[-1] <= time:
                st.pop()

            st.append(time)

        return len(st)
