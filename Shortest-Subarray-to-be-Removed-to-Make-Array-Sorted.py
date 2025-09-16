class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        j = len(arr)-1

        while j >0 and arr[j]>= arr[j-1]:
            j-=1

        ans =j
        i =0

        while (i<j and (i==0 or arr[i]>= arr[i-1])):
            while(j<len(arr) and arr[i]>arr[j]):
                j+=1

            ans = min(ans, j-i-1)
            i+=1
        
        return ans
        