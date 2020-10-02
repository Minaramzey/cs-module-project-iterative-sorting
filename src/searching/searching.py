def linear_search(arr, target):
    # Your code here
    for i in range (0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lower = 0
    upper = len(arr)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = arr[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

    return -1  # not found
