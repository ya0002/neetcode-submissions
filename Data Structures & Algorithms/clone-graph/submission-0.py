"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        node2 = Node(val=node.val)
        
        created = dict()
        created[node2.val] = node2

        to_process = [(node, node2)]

        while to_process: 
            old_node,new_node = to_process.pop()
            for n in old_node.neighbors:
                if n.val not in created:
                    created[n.val] = Node(val=n.val)
                    to_process.append((n,created[n.val]))
                new_node.neighbors.append(created[n.val])

        return node2