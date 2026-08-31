class Solution:
    def maxArea(self, height: List[int]) -> int:

        l =0
        r= len(height)-1

        left = height[l]
        right = height[r]

        maxi =0

        while l<r:

            if height[l]<=height[r]:
                area = (r-l) *height[l]
                l+=1
                maxi = max(maxi, area)

            else:
                area = (r-l)*height[r]
                r-=1
                maxi = max(maxi, area)

        return maxi
        