def quicksort(l):
    if len(l) < 2:
        return l
    else:
        p = l[0]
        left, right = [], []
        for x in range(1, len(l)):
            if l[x] < p:
                left.append(l[x])
            elif l[x] > p:
                right.append(l[x])
        left = quicksort(left)
        right = quicksort(right)
        l = [int(x) for x in left] + [p] + [int(x) for x in right]
        print(*l)
        return l


n = int(input())
arr = [int(x) for x in input().split()]
arr = quicksort(arr)