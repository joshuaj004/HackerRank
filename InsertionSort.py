l = int(input())
arr = [int(x) for x in input().split()]
for x in range(1, l):
    cmp = arr[x]
    for y in range(x, 0, -1):
        if cmp < arr[y-1]:
            arr[y] = arr[y-1]
            if y == 1:
                arr[y-1] = cmp
        else:
            arr[y] = cmp
            break
    print(*arr)