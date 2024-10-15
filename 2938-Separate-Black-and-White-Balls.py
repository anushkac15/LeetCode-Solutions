class Solution:
    def minimumSteps(self, s: str) -> int:
        total_step = 0
        black_count =0

        for char in s:
            if char =='0':
                total_step +=black_count
            else:
                black_count+=1
        return total_step