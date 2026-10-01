class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        cnt1 = 1
        maxi1 = 1

        for i in range(len(arr) - 1):
            if i % 2 == 0 and arr[i] < arr[i + 1]:
                cnt1 += 1
            elif i % 2 == 1 and arr[i] > arr[i + 1]:
                cnt1 += 1

            else:
                cnt1 = 1

            maxi1 = max(maxi1, cnt1)

        maxi2 = 1
        cnt2 = 1

        for i in range(len(arr) - 1):
            if i % 2 == 0 and arr[i] > arr[i + 1]:
                cnt2 += 1
            elif i % 2 == 1 and arr[i] < arr[i + 1]:
                cnt2 += 1
            else:
                cnt2 = 1

            maxi2 = max(maxi2, cnt2)

        return max(maxi1, maxi2)
