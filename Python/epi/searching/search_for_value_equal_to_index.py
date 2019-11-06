def search_entry_equal_to_its_index(A):
    left, right = 0, len(A)-1
    while left <= right:
        mid = (left + right) / 2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1
