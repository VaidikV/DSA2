# Last updated: 10/6/2025, 12:02:17 PM
'''
Using Boyer Moore algo. 

This works only if the list HAS a majority number (in this case, yes). NC and DT
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using the boyer moore algo
        count = 0
        res = 0

        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1
        return res
        
        