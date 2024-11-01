class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums :
            if (target - i ) in nums:
                if i == target-i:
                    first =nums.index(i)
                    try:
                        second = nums.index(i,first+1,len(nums))
                        if first!=second:
                            return [first,second]
                    except:
                        continue
                else:
                    return [nums.index(i),nums.index((target-i))]


sol = Solution()
print(sol.twoSum( [3,2,4],6))
    

# l = [3,3]
# target = 6
# first =l.index(3)
# print(l.index(3))
# second = l.index(3,first+1,len(l))
# print(second)
          