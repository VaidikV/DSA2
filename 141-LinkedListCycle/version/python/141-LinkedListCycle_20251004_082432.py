# Last updated: 10/4/2025, 8:24:32 AM
'''
Using 2 pointers (single and double) The cycle makes them converge at some point. So when the two pointers are same, we conclude there is a cycle. also this approach makes the space constant. 
DT
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: 
            return False
        
        single = double = head
        while double and double.next is not None:
            double = double.next.next
            single = single.next
            if double == single:
                return True
        return False