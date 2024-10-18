class Solution:
    def plusOne(self, digits: list[int]) ->list[int]:
        foundOnlyNine = True
        cnt =0
        for element in digits:
            if element != 9:
                foundOnlyNine = False
        if foundOnlyNine :
            digits2 = []
            digits2.append(1)
            for i in range(len(digits)) :
                digits2.append(0)
            return digits2
        else:
            digits[-1]+=1
            if digits[-1] == 10:
                i = -1
                while digits[i] == 10 :
                    digits[i]= 0
                    digits[i-1] = digits[i-1]+1
                    i-=1
            return digits
        
sol = Solution()
print(sol.plusOne([9,9,9,9]))