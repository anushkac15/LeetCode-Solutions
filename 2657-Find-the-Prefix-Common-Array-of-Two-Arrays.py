class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        commonPre=0
        cnt = [0]*(n+1)
        res = [0]*n

        for i in range(n):
            cnt[A[i]] +=1
            if cnt[A[i]]==2:
                commonPre+=1
            cnt[B[i]]+=1
            if cnt[B[i]]==2:
                commonPre+=1
            res[i]=commonPre
        return res

        