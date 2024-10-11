class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if not matrix or not matrix[0]:
            return res
        row = len(matrix)
        column= len(matrix[0])
        top = 0
        right = column -1
        bottom = row-1
        left = 0

        while top<= bottom and left<=right :

            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            if top <= bottom:
                for i in range(right, left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            
            if left<=right:
                for i in range(bottom, top-1,-1):
                    res.append(matrix[i][left])
                left+=1

        return res      