class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1+nums2)
        n = len(merge)
        if(n%2==1):
            return float(merge[n//2])
        else:
            mid1 = (merge[n//2])
            mid2 = (merge[n//2-1])
            return( float (mid1+mid2)/2.0)

        