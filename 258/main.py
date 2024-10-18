class Solution:
    def addDigits(self, num: int) -> int:
        result = num%9
        if num==0:
            return 0
        elif result==0:
            return 9
        else:
            return result