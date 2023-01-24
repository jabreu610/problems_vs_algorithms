from random import randrange

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    """
    last_zero_index = 0
    ans = []
    for val in input_list:
        if val == 0:
            ans = [val] + ans
            last_zero_index += 1
        if val == 2:
            ans += [val]
        if val == 1:
            ans = ans[:last_zero_index] + [val] + ans[last_zero_index:]

    return ans


if __name__ == "__main__":

    print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
          == sorted([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
    # True
    print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) == sorted(
        [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
    # True
    print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == sorted(
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
    # True
    print(sort_012([2, 1, 0]) == sorted([2, 1, 0]))
    # True
    print(sort_012([2, 1]) == sorted([2, 1]))
    # True
    print(sort_012([1, 0]) == sorted([1, 0]))
    # True
    print(sort_012([2, 0]) == sorted([2, 0]))
    # True
    print(sort_012([]) == sorted([]))
    # True
    long_input = [randrange(3) for _ in range(2 ** 8)]
    print(sort_012(long_input) == sorted(long_input))
    # True
