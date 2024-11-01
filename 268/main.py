#intervalul [0,n]
# n fiind len de array

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Rezolvare cu dictionar, dar ineficient
        sum = 0
        for nr in nums:
            sum += nr
        return abs(sum - ((len(nums)*(len(nums)+1))//2))
        # dict = {x : x in nums for x in range(n+1)}
        # for x,cond in dict.items():
        #     if cond == False:
        #         return x
        

            




sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))


# arr = [9,6,4,2,3,5,7,0,1]
# print(sum(arr))
# 