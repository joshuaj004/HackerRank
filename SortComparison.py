def insertion_sort(arr):
    counter = 0
    for x in range(1, len(arr)):
        cmp = arr[x]
        for y in range(x, 0, -1):
            if cmp < arr[y-1]:
                arr[y] = arr[y-1]
                counter += 1
                if y == 1:
                    arr[y-1] = cmp
            else:
                arr[y] = cmp
                break
        #print(*arr)
    return counter

def quicksort(A, lo, hi):
    swaps = [0]
    if lo < hi:
        p = partition(A, lo, hi, swaps)
        swaps += quicksort(A, lo, p - 1)
        swaps += quicksort(A, p + 1, hi)
    return swaps
        
def partition(A, lo, hi, swaps):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i] 
            swaps[0] += 1
            i += 1
    A[i], A[hi] = A[hi], A[i] 
    swaps[0] += 1
    return i


n = int(input())
A = [int(x) for x in input().split()]
B = A[:]
ins = insertion_sort(B)
quick = sum(quicksort(A, 0, n - 1))
print(ins - quick)