class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to store num and frequency
        count = defaultdict(int)

        # count frequencies
        for num in nums:
            count[num] += 1

        # sort by frequency (highest first)
        sorted_count = sorted(count.items(), key=lambda pair: pair[1], reverse=True)

        result = []

        for num, freq in sorted_count[:k]:
            result.append(num)

        return result