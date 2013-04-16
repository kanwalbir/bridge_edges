#-----------------------------------------------------------------------------#

"""
Post order every node in the tree in order of left node first, then right 
node, and then finally the root.

Args: (i)  Tree in dictionary format
      (ii) Starting node of the tree called root

Returns: (i) Post order value of every node in the tree in dictionary format
"""
def post_order(S, root):
    current_post = 1
    po = {}
    to_assign = [root]
    while to_assign:
        check = to_assign[:]
        r = to_assign[-1]

        for node in S[r]:
            if node not in to_assign and node not in po:
                if S[r][node] == 'green':
                    to_assign.append(node)
        
        if to_assign == check:
            to_assign.pop()
            po[r] = current_post
            current_post += 1
    return po

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
print po
assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
"""
#-----------------------------------------------------------------------------#
