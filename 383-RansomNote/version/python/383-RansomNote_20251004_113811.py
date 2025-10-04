# Last updated: 10/4/2025, 11:38:11 AM
'''
Entirely my answer using 1 dictionary to count the chars in magazine. Then reducing the number when found in ransom note.

I think this is inefficient.
'''

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