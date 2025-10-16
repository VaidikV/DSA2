# Last updated: 10/15/2025, 10:44:13 PM
# max_sub = nums[0] caught me off guard. But understand that the smallest array here can be an array with just 1 element. In that case, the sum will be the first element. Hence max_sub = nums[0]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm!

        max_sub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            max_sub = max(max_sub, curSum)
        return max_sub