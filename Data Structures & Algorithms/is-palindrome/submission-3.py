class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean =""
        #check is char is letter/num and if so, convert to lowercase and add to new string
        for char in s:
            if char.isalnum():
                clean += char.lower()
        #two pointers, add left to beginning of string and right to end
        left = 0
        right = len(clean)-1
        #print(left,right,clean[left],clean[right])
        #comparison
        while left<right:
            if clean[left]==clean[right]:
                left+=1
                right-=1
                print(left,right,clean[left],clean[right])
                continue
        
            else:
                return False
                break
        return True
