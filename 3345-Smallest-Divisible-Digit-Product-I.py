class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def check(num:int)->bool:

            pro =1 

            while num>0:
                pro*=num%10
                num//=10

                if pro==0:
                    break
            return pro%t==0

        while not check(n):
            n+=1

        return n
        