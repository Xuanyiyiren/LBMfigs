import numpy as np

a = np.array([
    [
        [26,10,22],
        [14,2,12],
        [24,8,20]
    ],
    [
        [18,4,16],
        [6,0,5],
        [17,3,15]
    ],
    [
        [25,9,21],
        [13,1,11],
        [23,7,19]
    ]
])

af = a.flatten()
print(af)

def c2i(cx, cy, cz):
    return a[cx + 1, cy + 1, cz + 1]

def c2if(cx, cy, cz):
    return af[9*cx + 3*cy + cz + 13]
    # return af[((cx + 1) * 9) + ((cy + 1) * 3) + (cz + 1)]

#
print(c2i(0,0,0))

print(c2i(1,0,0))
print(c2i(-1,0,0))
print(c2i(0,1,0))
print(c2i(0,-1,0))
print(c2i(0,0,1))
print(c2i(0,0,-1))

print(c2i(1,1,0))
print(c2i(-1,1,0))
print(c2i(1,-1,0))
print(c2i(-1,-1,0))
print(c2i(1,0,1))
print(c2i(-1,0,1))
print(c2i(1,0,-1))
print(c2i(-1,0,-1))
print(c2i(0,1,1))
print(c2i(0,-1,1))
print(c2i(0,1,-1))
print(c2i(0,-1,-1))

print(c2i(1,1,1))
print(c2i(-1,1,1))
print(c2i(1,-1,1))
print(c2i(-1,-1,1))
print(c2i(1,1,-1))
print(c2i(-1,1,-1))
print(c2i(1,-1,-1))
print(c2i(-1,-1,-1))

#
print(c2if(0,0,0))

print(c2if(1,0,0))
print(c2if(-1,0,0))
print(c2if(0,1,0))
print(c2if(0,-1,0))
print(c2if(0,0,1))
print(c2if(0,0,-1))

print(c2if(1,1,0))
print(c2if(-1,1,0))
print(c2if(1,-1,0))
print(c2if(-1,-1,0))
print(c2if(1,0,1))
print(c2if(-1,0,1))
print(c2if(1,0,-1))
print(c2if(-1,0,-1))
print(c2if(0,1,1))
print(c2if(0,-1,1))
print(c2if(0,1,-1))
print(c2if(0,-1,-1))

print(c2if(1,1,1))
print(c2if(-1,1,1))
print(c2if(1,-1,1))
print(c2if(-1,-1,1))
print(c2if(1,1,-1))
print(c2if(-1,1,-1))
print(c2if(1,-1,-1))
print(c2if(-1,-1,-1))
