class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dict = {}
        st = []

        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<= nums2[i]:
                st.pop()

            if st :
                dict[nums2[i]] = st[-1]
            else:
                dict[nums2[i]] = -1

            st.append(nums2[i])

        return [dict[num] for num in nums1]
        