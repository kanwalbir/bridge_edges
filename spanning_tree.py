#-----------------------------------------------------------------------------#

"""
Starting from the root and using depth first search, nodes and edges are 
added to the tree. G[n1][n2] == 1 implies that there was an edge between n1 
and n2. If the node is encountered for the first time, the edge is marked 
green, otherwise the edge is marked red. 

Args: (i)  Graph in dictionary format
      (ii) Starting node of the graph called root

Returns: (i) Tree in dictionary format
"""
def create_rooted_spanning_tree(G, root):
    visited, to_visit = [], [root]
    S = {}
    for node in G:
        S[node] = {}

    while to_visit:
        r = to_visit.pop(0)
        visited.append(r)

        for node in G[r]:
            if r+node not in visited:
                visited += [r+node, node+r]

                if node not in to_visit and node not in visited:
                    S[r][node] = S[node][r] = 'green'
                    to_visit.append(node)
                else:
                    S[r][node] = S[node][r] = 'red'
    return S

#-----------------------------------------------------------------------------#

"""
Test values and assert statements for above function.
"""
"""
G = {'a': {'c': 1, 'b': 1}, 
     'b': {'a': 1, 'd': 1}, 
     'c': {'a': 1, 'd': 1}, 
     'd': {'c': 1, 'b': 1, 'e': 1}, 
     'e': {'d': 1, 'g': 1, 'f': 1}, 
     'f': {'e': 1, 'g': 1},
     'g': {'e': 1, 'f': 1}}

S = create_rooted_spanning_tree(G, 'a')
print S
assert S == {'a': {'c': 'green', 'b': 'green'}, 
             'b': {'a': 'green', 'd': 'red'}, 
             'c': {'a': 'green', 'd': 'green'}, 
             'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
             'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
             'f': {'e': 'green', 'g': 'red'},
             'g': {'e': 'green', 'f': 'red'}}
"""
#-----------------------------------------------------------------------------#
