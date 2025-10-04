# Last updated: 10/4/2025, 12:54:26 PM
# Figuring out that fibonacci sequence is underlying cause here. Hence using fibonacci sequence code. DT
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1, 2]
        for step in range(3, n + 1):
            ways.append(ways[step - 1] + ways[step - 2])
        return ways[n]