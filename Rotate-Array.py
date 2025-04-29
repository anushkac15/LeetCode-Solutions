class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        n = len(nums)
        k = k%n

        def reverse(left,right):
            while(left<=right):
                nums[left], nums[right] = nums[right], nums[left]
                left=left+1
                right = right-1

        reverse(0,n-k-1)
        reverse(n-k,n-1)
        reverse(0,n-1)