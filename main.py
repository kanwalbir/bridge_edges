#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Other Python file imports.
"""
from spanning_tree import create_rooted_spanning_tree
from post_order import post_order
from ancestors import create_ancestors
from descendants import number_of_descendants
from po_low_high import po_low_high

#-----------------------------------------------------------------------------#

"""
Find all the bridge edges in the graph by calling all the modules in 
following order:
- create_rooted_spanning_tree (create a tree based on the graph)
- post_order (find the post order values of every node in the tree)
- create_ancestors (find all the ancestors for every node)
- number_of_descendants (find the number of descendants for every node)
- po_low_high (find the lowest and highest post order values for every node)

Calculate the bridge edges using following formula:
- [h_value <= po_value] AND [l_value > ABS(nd_value - po_value)]

Args: (i)  Graph in dictionary format
      (ii) Starting node of the graph called root

Returns: (i) All the bridge edges in the graph as list of tuples
"""
def bridge_edges(G, root):
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    ancestors = create_ancestors(S, root)
    nd = number_of_descendants(S, root)
    l, h = po_low_high(S, root, po)

    bridges = []
    for node in S:
        for n in S[node]:
            if n not in ancestors[node]:
                if S[node][n] == 'green':
                    if h[n] <= po[n]:
                        if l[n] > abs(nd[n]-po[n]):
                            bridges.append((node, n))
    return bridges

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above function.
"""

G = {'a': {'c': 1, 'b': 1}, 
     'b': {'a': 1, 'd': 1}, 
     'c': {'a': 1, 'd': 1}, 
     'd': {'c': 1, 'b': 1, 'e': 1}, 
     'e': {'d': 1, 'g': 1, 'f': 1}, 
     'f': {'e': 1, 'g': 1},
     'g': {'e': 1, 'f': 1}}

bridges = bridge_edges(G, 'a')
print "\n", "The Graph is:", G, "\n"
print "The Bridge Edge for this graph is:", bridges, "\n"
assert bridges == [('d', 'e')]
#-----------------------------------------------------------------------------#
