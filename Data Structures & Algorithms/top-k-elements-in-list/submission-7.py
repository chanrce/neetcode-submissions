class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer=[]
        freq=defaultdict(int)
        #loop through array
        for val in nums:
            # add to hashmap with count
            freq[val]+=1
        res=sorted(freq.items(),reverse=True,key=lambda x:x[1])
        
        #return the keys corresponding to those values
        
        for values in res[:k]:
            answer.append(values[0])
        return answer

            