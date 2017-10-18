from random import randint
import sys
A = [randint(0, 99) for x in range(0,9)]

def merge(A, B):
    C = []
    A.append(sys.maxsize)
    B.append(sys.maxsize)
    while len(A) != 1 or len(B) != 1:
        if A[0] < B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    return C

def mergeSort(A):
    if(len(A)==1):
        return A
    mid = len(A)//2
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

# Complexity: O( n*log(n) )
def lower_median_V1(A, p, r):
    A[p:r+1] = mergeSort(A[p:r+1])
    median_index = (r-p+1)//2+p
    return A[median_index]

def random_partition(A, p, r):
    pivot_index = randint(p, r)
    B = A[:]
    lower = p
    bigger = r
    for x in range(p,r+1):
        if x != pivot_index:
            if B[x] > B[pivot_index]:
                A[bigger] = B[x]
                bigger = bigger-1
            else:
                A[lower] = B[x]
                lower = lower+1
    A[lower] = B[pivot_index]
    return A, lower

def select_kth_lower(A, p, r, i):
    if p == r:
        return A[p]
    A, index_pivot = random_partition(A, p, r)
    if index_pivot == i:
        return A[index_pivot]
    else:
        if i < index_pivot:
            return select_kth_lower(A, p, index_pivot-1, i)
        else:
            return select_kth_lower(A, index_pivot+1, r, i)


# Complexity: O( n )
def lower_median_V2(A, p, r):
    return select_kth_lower(A, p, r, (r-p+1)//2+p)

print("Lower Median_V1: ", lower_median_V1(A, 0, len(A)-1))
print("Lower Median_V2: ", lower_median_V2(A, 0, len(A)-1))
