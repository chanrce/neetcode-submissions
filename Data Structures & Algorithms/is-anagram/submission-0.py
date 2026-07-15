class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}

        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for j in t:
            if j in seen and seen[j]>0:
                seen[j]-=1
            else:
                return False
        for val in seen.values():
            if val !=0:
                return False
        return True
