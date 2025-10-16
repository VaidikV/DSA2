# Last updated: 10/15/2025, 10:18:05 PM
# ig the most efficient.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False