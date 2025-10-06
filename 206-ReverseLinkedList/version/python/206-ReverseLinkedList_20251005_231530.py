# Last updated: 10/5/2025, 11:15:30 PM
# recursion - DT
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)
    def helper(self, prev, curr):
        if not curr:
            return prev
        
        nxt = curr.next
        curr.next = prev
        new_head = self.helper(curr, nxt)

        return new_head




