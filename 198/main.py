class Solution:
    def hammingWeight(self, n: int) -> int:
        bits=0
        while n>0:
            if n%2==1:
                bits+=1
            n//=2
        return bits
    
sol = Solution()
print(sol.hammingWeight(11))