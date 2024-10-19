class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0"

        length = pow(2,n) -1

        if(k<(length//2+1)):
            return self.findKthBit(n-1,k)

        if(k==(length//2+1)):
            return "1"

        else:
            ch = self.findKthBit(n-1,length-k+1)
            if ch=="0":
                return "1"
            else:
                return "0"