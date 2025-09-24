# Last updated: 9/23/2025, 11:59:49 PM
# Brute force approach
class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
        # stack = []
        # close_to_open = {'}' : '{', ')' : '(', ']' : '['}

        # for i in s:
        #     if i in close_to_open:
        #         if stack and stack[-1] == close_to_open[i]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(i)
        # return True if not stack else False