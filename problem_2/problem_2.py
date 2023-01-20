def rotated_array_search(arr, target):
    """Returns the index of the target value if found within a sorted and rotated array."""
    lower = 0
    upper = len(arr) - 1
    pivot = None
    while lower <= upper:
        mid = (lower + upper) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        if mid > 0 and mid_val < arr[mid - 1]:
            pivot = mid
            break
        elif mid_val < arr[0]:
            upper = mid - 1
        elif mid_val > arr[-1]:
            lower = mid + 1

    sorted_arr = arr[pivot:] + arr[:pivot]
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        mid_val = sorted_arr[mid]

        if mid_val == target:
            return (mid + pivot) % len(arr)
        elif mid_val < target:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


if __name__ == "__main__":
    print(rotated_array_search([5, 1, 2, 3, 4], 2) == 2)
    # True
    print(rotated_array_search([4, 5, 1, 2, 3], 5) == 1)
    # True
    print(rotated_array_search([3, 4, 5, 1, 2], 2) == 4)
    # True
    print(rotated_array_search([2, 3, 4, 5, 1], 5) == 3)
    # True
    print(rotated_array_search([2, 3, 4, 5, 1], 6) == -1)
    # True
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6) == 0)
    # True
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1) == 5)
    # True
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1) == 3)
    # True
    print(rotated_array_search([3, 1], 1) == 1)
    # True
    long_array = [x for x in range(2**8, 2**16, 4)] + \
        [x for x in range(0, 2**8, 4)]
    print(rotated_array_search(long_array, 512) == 64)
    # True
    print(rotated_array_search([], 100) == -1)
    # True
