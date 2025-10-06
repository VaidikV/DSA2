# Last updated: 10/6/2025, 11:44:45 AM
# Just a basic dict solution I came up with on the fly. I think I can make this even more efficient.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
            if count[n] > (len(nums) // 2):
                return n
        
        
        