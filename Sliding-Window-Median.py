class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        res =[]
        window = SortedList()

        for i in range(len(nums)):

            window.add(nums[i])

            if i>=k:
                window.remove(nums[i-k])

            if i>=k-1:
                if k%2==1:
                    res.append(window[k//2])
                else:
                    res.append((window[k//2]+window[k//2-1])/2)

        return res


        