# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head=None

        prev=None  
        carry = 0

        while l1 or l2:

            
            l1v= l1.val if l1 else 0
            l2v=l2.val if l2 else 0

            d_sum = l1v+l2v+carry

            node_val = d_sum %10
            carry= d_sum//10

            new_node = ListNode(val=node_val)

            if not head:
                head = new_node
            else:
                prev.next = new_node
            
            prev = new_node

            l1 = l1.next if l1 else None
            l2=l2.next if l2 else None
        
        ## handle the last carry
        if carry!=0:
            new_node = ListNode(val=carry)
            prev.next = new_node
        
        return head


        