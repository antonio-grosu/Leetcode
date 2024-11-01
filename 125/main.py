class Solution:
    def isPalindrome(self, s: str) -> bool:
        newList = [chr.lower() if chr.isalpha() or chr.isdigit() else '' for chr in s]
        prop2 = ''.join(newList)
        prop3 = prop2[::-1]
        return prop3 == prop2



sol = Solution()
print(sol.isPalindrome("0P"))