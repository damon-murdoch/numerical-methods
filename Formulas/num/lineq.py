# a,b,c: vectors(3): int, x,y,z: int

def det(A):
    D11 = (A[2][2] * A[3][3]) - (A[3][2] * A[2][3])
    D12 = (A[2][1] * A[3][3]) - (A[3][1] * A[2][3])
    D13 = (A[2][1] * A[3][2]) - (A[3][1] * A[2][2])
    return D11 - D12 + D13

def cramers(a,b,c,x,y,z):
    pass