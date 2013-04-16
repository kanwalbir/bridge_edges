#-----------------------------------------------------------------------------#
#                            Bridge Edges                                     #
#-----------------------------------------------------------------------------#

PROBLEM: Find the bridge edges of a connected graph.

A bridge edge of a connected graph (no set of nodes are isolated from one another) is the edge whose removal disconnects the graph from being a one big connected piece. For example, in a social network if two people stopped being friends and this breakup causes a disconnection in that network, then that particular friendship is a bridge edge of that social network.

SOLUTION: The solution is implemented using the following algorithm suggested by Robert Tarjan in 1974:

1. Write the graph as a rooted spanning tree
2. Post order all the nodes of the tree - (po_value)
3. Compute number of descendants for each node - (nd_value)
4. Find the lowest post order value for each node - (l_value)
5. Find the highest post order value for each node - (h_value)
6. Bridge edge is calculated based on following:
    [h_value <= po_value] AND [l_value > ABS(nd_value - po_value)]


SOURCE: http://en.wikipedia.org/wiki/Bridge_(graph_theory)

IMPLEMENTATION: python main.py
#-----------------------------------------------------------------------------#
