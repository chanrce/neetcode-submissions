class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #create set of existing characters
        chars=set(s)
        #create best
        best=0
        
        # go thru string with sliding window looking for one char, say "X"
        for char in chars:
            l=0
            count=0
            #for each X add to count
            for r in range(len(s)):
                if char==s[r]:
                    count+=1
                # compare to (window size -count) to k, if <= k then move right pointer
                if (r-l+1)-count<=k:
                    best=max(best,r-l+1)
                    continue
                #if more than k, move left pointer and subtract from count IF l==x
                #record best
                else:
                    if s[l]==char:
                        count-=1
                    l+=1
        #return best
        return best
            
                
        