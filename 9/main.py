class Solution:
    def isPalindrome(self, x: int) -> bool:
        cx = x
        ogl = 0
        if x>=0:
            while x > 0:
                ogl = ogl*10
                ogl += x%10
                x//=10
            if ogl == cx:
                return True
            else:
                return False
        else :
            return False
    
sol = Solution()
print(sol.isPalindrome(1231))

