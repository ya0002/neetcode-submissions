# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ## find the midpoint
        s,f = head,head.next
        while f and f.next:
            s= s.next
            f= f.next.next
        
        ## reverse linked list from s.next; flip all nexts after s(mid point)
        cur=s.next
        prev=None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev=cur
            cur= temp


        ## MERGE
        s.next=None
        curr=head
        curr2=prev ## since prev = last cur, whihc would be the last element
        ## we are merging in the curr2 list whihc would be equal or smaller 
        while curr2:

            temp1= curr.next
            curr.next = curr2
            curr = temp1


            temp2= curr2.next
            curr2.next= curr
            curr2 = temp2

  

        