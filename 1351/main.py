class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        cnt=0
        n = len(grid)
        m  = len(grid[0])
        for i in range(n):
            current_list = grid[i]
            for j in range(m):
                if current_list[j] < 0:
                    cnt +=1
        return cnt


sol = Solution()
print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))