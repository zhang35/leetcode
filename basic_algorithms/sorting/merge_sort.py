def merge(arr, left, mid, right):
    L = arr[left: mid + 1]
    R = arr[mid + 1: right + 1]

    # Initialize pointers for L[], R[], and merged array
    i, j, k = 0, 0, left

    # Merge the temporary arrays back into arr[left..right]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[] and R[]
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
	if l < r:
		# Same as (l+r)//2, but avoids overflow for large l and h
		m = l + (r - l) // 2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


arr = [1, 7, 4, 1, 10, 9, -2]
print(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
