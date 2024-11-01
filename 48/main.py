class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        firstLine = matrix[0]
        m=len(firstLine)
        cnt=0

        # o   de la coada cu vectorii si apoi de la inceput la final
        b=matrix.copy()
        while cnt < m :
            newLine = []
            for i in range(n-1,-1,-1):
                currentLine = b[i]
                newLine.append(currentLine[cnt])
                # print(cnt,i)
            matrix[cnt] = newLine
            cnt+=1
      




# for i in range(3-1,-1,-1):
#     print(i)


sol = Solution()
print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

[[7,4,1]]