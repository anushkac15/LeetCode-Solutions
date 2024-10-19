class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k==1:
            return 0

        length = pow(2,n-1)

        if k<=(length//2):
            return self.kthGrammar(n-1,k)
        else:
            ch = self.kthGrammar(n-1,k-length//2)
            if ch ==0:
                return 1
            else:
                return 0
