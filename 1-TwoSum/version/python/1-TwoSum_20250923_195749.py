# Last updated: 9/23/2025, 7:57:49 PM
# Brute Force approach. Just add the current element with every other element and see if it similar to the target. If yes, just return the index of both
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        hm = {}

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hm:
        #         return [hm[diff], i]
        #     hm[n] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]