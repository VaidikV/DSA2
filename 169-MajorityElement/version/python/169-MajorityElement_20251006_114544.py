# Last updated: 10/6/2025, 11:45:44 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
            if count[n] > (len(nums) // 2):
                return n
        
        
        