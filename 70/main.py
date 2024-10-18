class Solution:
    def climbStairs(self, n: int) -> int:
        x1 =1
        x2 =1
        res =1
        for i in range (n-2):
            res = x1+x2
            x2=x1
            x1 = res
        return res
    

sol = Solution()
print(sol.climbStairs(4))
# def fib(n: int):
#     x1 =1
#     x2 =1
#     res =1
#     for i in range (n-2):
#         res = x1+x2
#         x2=x1
#         x1 = res
#     return res
# print(fib(5))