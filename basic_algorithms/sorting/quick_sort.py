def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        p = partition(array, low, high)

        quickSort(array, low, p - 1)

        quickSort(array, p + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print(data)

quickSort(data, 0, len(data)-1)
print(data)