class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mp = {}

        st = []

        for i in range(len(nums2)-1, -1, -1):

            while st and st[-1] <= nums2[i]:
                st.pop()

            if st:
                mp[nums2[i]] = st[-1]
            else:
                mp[nums2[i]] = -1

            st.append(nums2[i])

        return [mp[num] for num in nums1]