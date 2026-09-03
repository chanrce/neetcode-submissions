class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #track the longest count
        longest = 0
        #make a set of nums for fast lookup
        num_set=set(nums)
        #go through nums
        for num in nums:
            #if num-1 not in set, start sequence
            if num-1 not in num_set:
                count = 1
                next_num=num+1
                while next_num in num_set:
                    count+=1
                    next_num+=1
                #update longest if longest
                if count>longest:
                    longest=count
        return longest
                

        