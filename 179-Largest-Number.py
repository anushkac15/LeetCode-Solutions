class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        s = [str(num) for num in nums]

        def comparator(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1

        s.sort(key=cmp_to_key(comparator))
        ans = \\.join(s)

        if ans[0]==\0\:
            return '0'
        else:
            return ans
        
        