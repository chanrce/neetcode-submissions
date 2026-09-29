class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closing = {")":"(","}":"{","]":"["}

        for c in s:
            if c not in closing:
                stack.append(c)
            else:
                if stack and stack[-1]==closing[c]:
                    stack.pop()
                else:
                    return False
        return not stack