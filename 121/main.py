class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        mi = float('inf')
        for v in prices :
            ans = max(ans, v-mi)
            mi = min(mi,v)
        return ans



sol = Solution()
print(sol.maxProfit([7,3,2,234,2]))