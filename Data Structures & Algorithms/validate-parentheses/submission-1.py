class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        #map the closing parentheses to open
        #bc you're looking up the closing parentheses
        hashmap={"]":"[",")":"(","}":"{"}
        
        for char in s:
            if char in hashmap:
                # if stack not empty
                if stack and stack[-1]==hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack: 
            return False
        else: 
            return True
                
