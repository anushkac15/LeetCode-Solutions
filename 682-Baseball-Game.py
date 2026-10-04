class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points=[]
        for i in operations:
            if i=='C':
                points.pop()
            elif i=='D':
                points.append(points[-1]*2)
            elif i=='+':
                points.append(points[-1]+points[-2])
            else:
                points.append(int(i))
        return sum(points)