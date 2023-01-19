def sqrt(num: int) -> int:
    """Returns the floored square root of a provided integer."""
    if num < 0:
        raise ValueError(
            """Math domain error. Unable to compute the square root of 
            negative numbers, complex numbers are not supported by this implementation""")
    elif num <=1:
        return num

    upper_bound = num // 2
    lower_bound = 0

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound ) // 2
        square = mid ** 2

        if square > num:
            upper_bound = mid - 1
        elif square < num:
            lower_bound = mid + 1
        else:
            return mid
    
    return upper_bound



if __name__ == "__main__":
    print(sqrt(25) == 5)
    # True
    print(sqrt(2**52) == 67108864)
    # True
    print(sqrt(2**52 + 1) == 67108864)
    # True
    print(sqrt(3) == 1)
    # True
    print(sqrt(2) == 1)
    # True
    print(sqrt(1) == 1)
    # True
    print(sqrt(0) == 0)
    # True
    try:
        sqrt(-25)
    except ValueError as e:
        print(e)
    # Math domain error. Unable to compute the square root of negative numbers, complex numbers are not supported by this implementation
