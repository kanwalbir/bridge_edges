#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Other Python file imports.
"""
from ancestors import create_ancestors

#-----------------------------------------------------------------------------#

"""
Find the number of descendants for every node in the tree which is equal to 
sum of the number of descendants of that node's children plus 1 (node itself).

Args: (i)  Tree in dictionary format
      (ii) Starting node of the tree called root

Returns: (i) Number of descendants of every node in the tree in dictionary format
"""
def number_of_descendants(S, root):
    nd = {}
    for node in S:
        nd[node] = 0
    
    ancestors = create_ancestors(S, root)
    for node in nd:
        for a in ancestors:
            if node in ancestors[a]:
                nd[node] += 1
    return nd

#-----------------------------------------------------------------------------#
"""
Test values and assert statements for above function.
"""
"""
S =  {'a': {'c': 'green', 'b': 'green'}, 
      'b': {'a': 'green', 'd': 'red'}, 
      'c': {'a': 'green', 'd': 'green'}, 
      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
      'f': {'e': 'green', 'g': 'red'},
      'g': {'e': 'green', 'f': 'red'}}

nd = number_of_descendants(S, 'a')
print nd
assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
"""
#-----------------------------------------------------------------------------#
