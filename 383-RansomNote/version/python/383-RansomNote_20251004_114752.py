# Last updated: 10/4/2025, 11:47:52 AM
# This was the same in other official solutions as well. Feeling great.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = {}
        for c in magazine:
            count_mag[c] = count_mag.get(c, 0) + 1
        for c in ransomNote:
            if c in count_mag and count_mag[c] != 0:
                count_mag[c] -= 1
            else:
                return False
        return True
