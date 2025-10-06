# Last updated: 10/5/2025, 8:13:40 PM
'''
Here we are using a default dict to keep a track of the counts of the chars to see if we can make a palindrome. Interesting obs: we can have only 1 odd count of a letter. It will stay in the middle while the others will be equally divided on the sides of the odd. 

NC
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        
        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        return res