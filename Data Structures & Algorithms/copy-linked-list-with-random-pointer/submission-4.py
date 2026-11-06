"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def get_node_vals_tuple(self,node):
        if not node:
            return (None,None,None)

        return (
            node.val if node.val else None,
            node.next.val if node.next else None,
            node.random.val if node.random else None,
        )

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        if head:
            head2 = Node(x=head.val)
        else:
            head2 = None

        created={
            # self.get_node_vals_tuple(head):head2
            head:head2
            }

        cur = head
        

        while cur:

            ## fetch or create the node
            cur_copy=None
            cur_k= cur#self.get_node_vals_tuple(cur)
            if cur_k in created:
                cur_copy=created[cur_k]
            else:
                cur_copy = Node(x=cur.val)
                created[cur_k] = cur_copy
            

            ## copy or create next node
            curn = cur.next
            curn_k= curn#self.get_node_vals_tuple(curn)
            curn_copy = None
            if curn_k in created:
                curn_copy=created[curn_k]
            elif curn:
                curn_copy = Node(x=curn.val)
                created[curn_k] = curn_copy
            
            ## copy or create random node
            curr = cur.random
            curr_k= curr#self.get_node_vals_tuple(curr)
            curr_copy = None
            if curr_k in created:
                curr_copy=created[curr_k]
            elif curr:
                curr_copy = Node(x=curr.val)
                created[curr_k] = curr_copy
            
            ## deep copy next and random nodes
            cur_copy.next = curn_copy
            cur_copy.random = curr_copy

            ## MOVE to next node
            cur = cur.next
        
        return head2
            
            
