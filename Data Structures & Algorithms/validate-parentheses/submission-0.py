class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep things ordered and stored
        stack = []
        # hashmap to map matching parentheses
        closeToOpen = {")": "(", "]" : "[", "}":"{"}


        for c in s:
            # if character is a closing parentheses
            if c in closeToOpen:
                # making sure stack is not empty
                # making sure value at top of stack [-1] aka last value added matches closing parentheses
                if stack and stack [-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                