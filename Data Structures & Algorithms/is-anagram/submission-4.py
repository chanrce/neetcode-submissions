class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # loop thru s and add all chars in s to a dict
        seen = {}

        for char in s:
            if char not in seen:
                seen[char]=0
            seen[char]+=1
            #print(seen)
        # loop thru t and check if those match dictionary vals or not
            # decrement from dict count each time it is seen
        #print("going thru t")
        for char in t:
            if char not in seen:
                return False
            if char in seen:
                seen[char]-=1
        # return true if everthing in dict is 0
        all_zeros = not any(seen.values())
       # print(all_zeros)
        return all_zeros