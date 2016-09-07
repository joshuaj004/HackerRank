// In-place quicksort with Lomuto Parition Scheme
// Helpful gif at https://upload.wikimedia.org/wikipedia/commons/8/84/Lomuto_animated.gif
def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)
        
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i] 
            i += 1
    A[i], A[hi] = A[hi], A[i] 
    print(*A)
    return i

n = int(input())
A = [int(x) for x in input().split()]
quicksort(A, 0, n - 1)