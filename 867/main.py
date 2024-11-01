class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        first_line = matrix[0]
        m = len(first_line)
        b=[]
        cnt=0
        while cnt <m:
            newLine = []
            for i in range(n):
                current_list = matrix[i]
                newLine.append(current_list[cnt])
            b.append(newLine)
            cnt+=1
        return b
    
sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
        