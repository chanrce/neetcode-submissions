class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = sorted(nums)

        left = 0
        right = len(copy) - 1

        while left < right:
            if copy[left] + copy[right] == target:
                first = nums.index(copy[left])
                second = nums.index(copy[right])

                if first == second:
                    second = nums.index(copy[right], first + 1)

                return sorted([first, second])

            elif copy[left] + copy[right] < target:
                left = left + 1

            else:
                right = right - 1

        return []