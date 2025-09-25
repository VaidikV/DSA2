# Last updated: 9/24/2025, 7:13:51 PM
'''
Make a new empty string. Go through each char in the og str and see if it is alphanumeric (using .isalnum() ) and then add it to the new string. 

If the newstring is same reversed, it is a palindrome. [::-1]
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse string (easy - using python fun)

        res_str = ''
        for c in s:
            if c.isalnum():
                res_str += c.lower()
        return res_str == res_str[::-1]
        