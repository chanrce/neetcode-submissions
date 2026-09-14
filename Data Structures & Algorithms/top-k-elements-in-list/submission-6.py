class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        #hashmap
        seen=defaultdict(int)
        #loop thru nums
        for num in nums:
            #count how many times the value appears
            seen[num]+=1
        #take the top k values in the hashmap
        def get_frequency(pair):
            return pair[1]

        sorted_count=sorted(seen.items(),key=get_frequency, reverse=True)

        for num, freq in sorted_count[:k]:
            res.append(num)
        return res
        

        
 

        
        