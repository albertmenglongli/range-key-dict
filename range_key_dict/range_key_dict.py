class RangeKeyDict:
    def __init__(self, my_dict):
        # !any(!A or !B) is faster than all(A and B)
        assert not any(map(lambda x: not isinstance(x, tuple) or len(x) != 2 or x[0] > x[1], my_dict))

        def lte(bound):
            return lambda x: bound <= x

        def gt(bound):
            return lambda x: x < bound

        # generate the inner dict with tuple key like (lambda x: 0 <= x, lambda x: x < 100)
        self._my_dict = {(lte(k[0]), gt(k[1])): v for k, v in my_dict.items()}

    def __getitem__(self, number):
        from functools import reduce
        _my_dict = self._my_dict
        try:
            result = next((_my_dict[key] for key in _my_dict if list(reduce(lambda s, f: filter(f, s), key, [number]))))
        except StopIteration:
            raise KeyError(number)
        return result

    def get(self, number, default=None):
        try:
            return self.__getitem__(number)
        except KeyError:
            return default


if __name__ == '__main__':
    range_key_dict = RangeKeyDict({
        (0, 100): 'A',
        (100, 200): 'B',
        (200, 300): 'C',
    })

    # test normal case
    assert range_key_dict[70] == 'A'
    assert range_key_dict[170] == 'B'
    assert range_key_dict[270] == 'C'

    # test case when the number is float
    assert range_key_dict[70.5] == 'A'

    # test case not in the range, with default value
    assert range_key_dict.get(1000, 'D') == 'D'

