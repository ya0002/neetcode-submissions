# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        curr= None

        while list1 or list2:
            
            to_append = None

            if list1 is None:
                to_append = list2 
                list2=list2.next
            elif list2 is None:
                to_append = list1
                list1=list1.next
            elif list1.val<=list2.val:
                to_append = list1 
                list1=list1.next
            else: 
                to_append = list2
                list2=list2.next
            
            if curr is None:
                curr = to_append
                head= to_append
            else:
                curr.next = to_append
                curr = to_append


        return head

        