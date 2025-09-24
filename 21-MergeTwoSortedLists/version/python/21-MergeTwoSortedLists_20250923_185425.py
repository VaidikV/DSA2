# Last updated: 9/23/2025, 6:54:25 PM
'''
First we create a new linked list. 

While list1 and list2 both have elements, we go through them and compare each and whichever is smaller is added to the new linked list we made. 

Then, the list from which we chose the smaller element, we update this list to move to the next element. 

Then, we move to the next element in our solution list so that we can add new element.

Once one of the list runs out of elements, we take a look at the other list, if it still has elements, we take all the rest of the elements from that list and add it to the solution list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2
        
        return dummy.next