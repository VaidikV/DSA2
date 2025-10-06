# Last updated: 10/5/2025, 8:17:04 PM
# Using a set for a smarter way of using the same logic from dict. NC

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)
            
        return res + 1 if seen else res