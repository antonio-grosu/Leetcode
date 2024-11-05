class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {x : s.count(x) for x in s}
        dict2 = {x : t.count(x) for x in t}
        return dict1==dict2



sol = Solution()
print(sol.isAnagram("a" , "aa"))





