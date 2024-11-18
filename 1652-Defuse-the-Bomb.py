class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        ans=[0]*n
        if k==0: return ans
        sign=-1
        if k>0:
            sign=1
        else:
            k=-k
        ans[0]=wsum=sum(code[sign:sign*(k+1):sign])
        for l in range(1, n):
            r=(l+k)%n
            wsum+=-code[sign*l]+code[sign*r]
            ans[sign*l]=wsum
        return ans