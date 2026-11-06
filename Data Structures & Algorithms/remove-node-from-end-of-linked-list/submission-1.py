# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        s,f=ListNode(next=head),head

        cnt=0
        while cnt<n and f:
            f=f.next
            cnt+=1

        
        while f:
            # print(s.val,f.val)
            s=s.next
            f=f.next
    
        
        
        if s.next is not head:
            s.next = s.next.next
        else:
            head=s.next.next

        # if s and s.next:
        #     s.next = s.next.next
        # else:
        #     return None

        return head