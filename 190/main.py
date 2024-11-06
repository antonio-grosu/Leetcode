class Solution:
    def reverseBits(self, n: int) -> int:
        str1 = "{0:b}".format(n)
        new_num =0

        str2=""

        if len(str1) < 32 :
            for i in range(32-len(str1)) :
                str2 += '0'
        str1 = str2 + str1

        for x in range(32) :
            if str1[x] == '1' :
                new_num += pow(2,x)

        return new_num    

sol = Solution()

print(sol.reverseBits(0b00000010100101000001111010011100))