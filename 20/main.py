# ideea principala este sa fac un dictionar pe care sa il verific daca cumva valoarea din stiva
# exista in el


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' :'(' ,
            ']' :'[' , 
            '}' : '{'
        }
        for char in s :
            if char in map:
                top_element = stack.pop() if stack else "#" # cazul in care s-a golit
                if top_element != map[char]:
                    return False
            else:
                stack.append(char)
        if(len(stack) == 0):
            return True
        else:
            return False

    


sol = Solution()
print(sol.isValid("()"))