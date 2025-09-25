# Last updated: 9/25/2025, 12:14:51 AM
# Method: sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorting
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        