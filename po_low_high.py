#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Other Python file imports.
"""
from ancestors import create_ancestors
from post_order import post_order

#-----------------------------------------------------------------------------#

"""
For every node in the tree, find the lowest and highest post order value 
below that node, including if possible one traversal along the red edge.

Args: (i)   Tree in dictionary format
      (ii)  Starting node of the tree called root 
      (iii) Post order value of every node in the tree in dictionary format

Returns: (i)  Lowest post order value for every node in dictionary format
         (ii) Highest post order value for every node in dictionary format
"""
def po_low_high(S, root, po):
    lpo, hpo = {}, {}
    ancestors = create_ancestors(S, root)
    reverse_po = dict(zip(po.values(),po))

    for i in range(1, len(reverse_po)+1):
        n = reverse_po[i]
        temp = [po[n]]
        
        for node in S[n]:
            if node not in ancestors[n]:
                temp.append(po[node])
                for x in S[node]:
                    if S[node][x] == 'red':
                        temp.append(po[x])
        lpo[n], hpo[n] = min(temp), max(temp)
        
    return lpo, hpo

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above function.
"""
"""
S = {'a': {'c': 'green', 'b': 'green'}, 
     'b': {'a': 'green', 'd': 'red'}, 
     'c': {'a': 'green', 'd': 'green'}, 
     'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
     'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
     'f': {'e': 'green', 'g': 'red'},
     'g': {'e': 'green', 'f': 'red'}}

po = post_order(S, 'a')
l, h = po_low_high(S, 'a', po)
print l
print h
assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}
assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
"""
#-----------------------------------------------------------------------------#
