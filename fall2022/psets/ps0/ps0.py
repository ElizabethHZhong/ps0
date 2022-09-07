#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
from shutil import register_unpack_format


class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # check if v is None
    if not v:
        return 0

    # base case: leaf node, where size is 1
    if not v.left and not v.right:
        v.size = 1

    # recursive call: vertex size is the sum of children + 1
    else:
        v.size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
    
    # return the size of the vertex
    return v.size


#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

def find_vertex(r):
    # check for r is None
    if not r:
        return r
    
    # store n/2 in a variable
    half = r.size / 2
    
    # both children exist
    if r.left and r.right:
        # base case: return the vertex if both child trees <= n/2
        if r.left.size <= half and r.right.size <= half:
            return r

        # reduce the potential function by moving to the larger child node
        elif r.left.size < r.right.size:
            return find_vertex(r.right)
        else:
            return find_vertex(r.left)

    # only left child exists
    elif r.left and not r.right:
        # base case: return the vertex if the child tree <= n/2
        if r.left.size <= half:
            return r
        # reduce the potential function by moving to the child node
        return find_vertex(r.left)

    # only right child exists
    elif not r.left and r.right:
        # base case: return the vertex if the child tree <= n/2
        if r.right.size <= half:
            return r
        # reduce the potential function by moving to the child node
        return find_vertex(r.right)

