class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict1 = {x:0 for x in nums}
        for x in nums:
            dict1[x] +=1
        for x,y in dict1.items():
            if y > 1 :
                return True
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))


