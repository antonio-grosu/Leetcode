class Solution:
    def fib(self, n: int) -> int:
        if(n>0):
            x1 =1
            x2 =1
            res =1
            for i in range (n-2):
                res = x1+x2
                x2=x1
                x1 = res
            return res
        else:
            return 0
    
