def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min_keys = min(d.keys())
    max_keys = max(d.keys())
    tuple = (min_keys, max_keys)
    return tuple

# ***OR:

    # keys = d.keys()

    # return (min(keys), max(keys))