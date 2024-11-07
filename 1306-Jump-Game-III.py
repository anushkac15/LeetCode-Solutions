class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def solve(start,visited):
            if start<0 or start>=len(arr):
                return False

            if arr[start]==0:
                return True

            if visited[start] ==1:
                return False

            visited[start]=1

            return solve(start+arr[start],visited) or solve(start-arr[start],visited)

        visited = [0]*len(arr)
        return solve(start,visited)