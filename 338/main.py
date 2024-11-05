class Solution:
    def countBits(self, n: int) -> list[int]:
        res =[]
        for i in range(n+1):
            bits=0
            while i > 0:
                if i%2==1:
                    bits+=1
                i//=2
            res.append(bits)
        return res
    

sol = Solution()
print(sol.countBits(5))