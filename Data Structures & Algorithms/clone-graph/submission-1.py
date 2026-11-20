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
        
        ## create the first entry node
        node2 = Node(val=node.val)
        
        ## add it to created hash map for checking and retreival
        created = dict()
        created[node2.val] = node2

        ## add it to proces for : copying over neighbours
        to_process = [(node, node2)]

        while to_process: 

            old_node,new_node = to_process.pop()

            for n in old_node.neighbors:

                if n.val not in created:
                    ## if the node doesnt exist then create it and add it to_process
                    created[n.val] = Node(val=n.val)
                    to_process.append((n,created[n.val]))

                new_node.neighbors.append(created[n.val]) ## add the copy of the neighbour, we migh update the neighbour's neighbours later if its in to_process

        return node2