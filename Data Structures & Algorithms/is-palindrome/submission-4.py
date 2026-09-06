class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert all to lowercase
        s=s.lower().replace(" ","")
        #left and right pointers
        left=0
        right=len(s)-1
        #go through input while L<r
        while left<right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].isalnum() and s[right].isalnum():
                #if chars are equal, move left pointer +1 and right -1
                if s[left]==s[right]:
                    left+=1
                    right-=1
                #else return false
                else:
                    return False
        #return true
        return True