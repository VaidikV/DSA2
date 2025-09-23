# Last updated: 9/23/2025, 10:16:06 AM
'''
using stack to keep track of the open parenthesis. Using hash-map for close-to-open parenthesis. 

First we add the opening parenthesis in the stack and when the corresponding closing parenthesis is seen, we grab the opening paren from the hashmap and then remove it from the stack. In the end, if the stack is empty, return True else False.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}' : '{', ')' : '(', ']' : '['}

        for i in s:
            if i in close_to_open:
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False