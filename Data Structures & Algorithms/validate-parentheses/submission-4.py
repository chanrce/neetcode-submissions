class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closing = {")":"(","}":"{","]":"["}

        for p in s:
            if p not in closing:
                stack.append(p)
            else:
                if stack and stack[-1]==closing[p]:
                    stack.pop()
                else:
                    return False
                    
        return not stack
