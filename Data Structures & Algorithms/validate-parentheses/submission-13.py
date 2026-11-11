class Solution:
    def isValid(self, s: str) -> bool:
        #create stack
        stack=[]
        #create hashmap
        hashmap={"(":")","{":"}", "[":"]"}
        if not len(s)%2==0:
            return False
        # go through string
        for char in s:
            # add parentheses to stack if char is an open parentheses (keys in the hashmap)
            if char in hashmap:
                stack.append(char)
            # else, it's a closing parentheses
            else:
                # look up that closing's opening parentheses and see if it's at the top of stack
                if stack and char==hashmap[stack[-1]]:
                    # if it is, pop the top of stack
                    stack.pop()
                    #else, return false
                else:
                    return False
        return not stack