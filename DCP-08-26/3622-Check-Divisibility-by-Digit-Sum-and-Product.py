class Solution:
    def checkDivisibility(self, n: int) -> bool:

        num =n
        sum =0
        pro =1 

        while n>0:
            rem = n%10
            sum+= rem
            pro*=rem
            n//=10

        total = sum+pro

        if num%total ==0:
            return True
        else:
            return False        