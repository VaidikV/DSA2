# Last updated: 10/4/2025, 1:43:22 PM
# Using dynamic programming programming. Concepts learnt: memoization (you don't need the entire array as used in the fibonacci sequence) we can just work with 2 values and update accordingly. Making space constant.
class Solution:
    def climbStairs(self, n: int) -> int:
        # ways = [1, 1, 2]
        # for step in range(3, n + 1):
        #     ways.append(ways[step - 1] + ways[step - 2])
        # return ways[n]

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

    
            