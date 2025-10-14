# Last updated: 10/13/2025, 8:04:30 PM
# Slow moves once and fast moves twice. when fast reaches the end (no next node), the slow will be at the middle. return slow.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow