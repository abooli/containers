def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''

    low, high, step = (0, 0, 1)

    if b is None and c is None:
        high = a
    elif c is None:
        (low, high) = (a, b)
    else:
        (low, high, step) = (a, b, c)

    x = low
    while x < high:
        yield x
        x += step
