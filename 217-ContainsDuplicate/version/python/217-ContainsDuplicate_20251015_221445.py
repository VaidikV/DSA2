# Last updated: 10/15/2025, 10:14:45 PM
# Using Hash set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use set!
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False