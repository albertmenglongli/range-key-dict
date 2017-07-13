# range_many_to_one_dict

This is a RangeDict using pure Python codes support Python2.7 and Python 3.X

pip install range-many-to-one-dict

```Python
from range_many_to_one_dict import RangeManyToOneDict

if __name__ == '__main__':
    range_dict = RangeManyToOneDict({
        (0, 100): 'A',
        (100, 200): 'B',
        (200, 300): 'C',
    })

    # test normal case
    assert range_dict[70] == 'A'
    assert range_dict[170] == 'B'
    assert range_dict[270] == 'C'

    # test case when the number is float
    assert range_dict[70.5] == 'A'

    # test case not in the range, with default value
    assert range_dict.get(1000, 'D') == 'D'
```
