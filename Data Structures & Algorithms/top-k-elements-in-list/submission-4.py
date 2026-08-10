class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,2,2,3], k=2
        # number -> how many times it appears
        # eg the number 1 appears 3 times in nums
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # creates empty list for each position in nums
        # we want buckets for each -- appears 1 time -> [], 2 times--> [], etc
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for cnt in range(len(freq) - 1, 0, -1):
            for num in freq[cnt]:
                res.append(num)
                if len(res) == k:
                    return res