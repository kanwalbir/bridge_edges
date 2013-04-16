#-----------------------------------------------------------------------------#

"""
Find all the ancestors for every node in the tree including itself.

Args: (i)  Tree in dictionary format
      (ii) Starting node of the tree called root

Returns: (i) All the ancestors of every node in the tree in dictionary format
"""
def create_ancestors(S, root):
    ancestors = {root:[root]}
    to_visit = [root]

    while to_visit:
        r = to_visit.pop()
        for node in S[r]:
            if node not in ancestors:
                if S[r][node] == 'green':
                    ancestors[node] = [node] + ancestors[r]
                    to_visit.append(node)
    return ancestors

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

ca = create_ancestors(S, 'a')
print ca
assert ca == {'a': ['a'], 
              'b': ['b', 'a'], 
              'c': ['c', 'a'], 
              'd': ['d', 'c', 'a'], 
              'e': ['e', 'd', 'c', 'a'], 
              'f': ['f', 'e', 'd', 'c', 'a'], 
              'g': ['g', 'e', 'd', 'c', 'a']}
"""
#-----------------------------------------------------------------------------#
