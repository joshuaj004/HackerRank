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
	
	
# Their Solution

def insertion_sort(l):
	# Iterate through list
    for i in range(1, len(l)):
		# Previous num
        j = i-1
		# Element to check
        key = l[i]
		# While previous num doesn't cause index error and key is less than current element
        while (j >= 0) and (l[j] > key):
		   # 'shift' elements
           l[j+1] = l[j]
		   # decrement j
           j -= 1
		# found the correct place for key, so it's inserted
        l[j+1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
