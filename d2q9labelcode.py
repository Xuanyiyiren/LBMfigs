import numpy as np

# D2Q9 label layout (cx rows, cy columns), cx, cy in {-1, 0, 1}
# Matches c2i_mat used in D2Q9LBMti.py
#
#   cy=-1   cy=0   cy=1
# cx=-1   [ 7,     4,     8 ]
# cx= 0   [ 3,     0,     1 ]
# cx= 1   [ 6,     2,     5 ]

a = np.array([
    [7, 4, 8],
    [3, 0, 1],
    [6, 2, 5],
], dtype=int)

af = a.flatten()
print(af)

def c2i(cx: int, cy: int) -> int:
    """Map lattice velocity (cx, cy) in {-1,0,1} to D2Q9 index.

    Axis-0 is cx, Axis-1 is cy.
    """
    return a[cx + 1, cy + 1]

def c2if(cx: int, cy: int) -> int:
    """Same mapping using flattened indexing formula (row-major).

    Equivalent to: af[((cx + 1) * 3) + (cy + 1)]
    """
    return af[3 * cx + cy + 4]

# Quick checks (should be 0..8 in the expected positions)
print(c2i(0, 0))
print(c2i(0, 1))
print(c2i(1, 0))
print(c2i(0, -1))
print(c2i(-1, 0))
print(c2i(1, 1))
print(c2i(1, -1))
print(c2i(-1, -1))
print(c2i(-1, 1))

# Flattened-index version checks
print(c2if(0, 0))
print(c2if(0, 1))
print(c2if(1, 0))
print(c2if(0, -1))
print(c2if(-1, 0))
print(c2if(1, 1))
print(c2if(1, -1))
print(c2if(-1, -1))
print(c2if(-1, 1))