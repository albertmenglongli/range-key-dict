# range-key-dict


Use ranges as key in dict, and the dict can be accessed by the number within the range, and get the value the range mapping to.

This is a RangeDict using pure Python codes support Python2.7 and Python 3.X

The looking up time on average is O(M) where M is the number of range keys in the dictionary.

install: pip install range-key-dict

```bash
pip install range-key-dict
```

```Python
from range_key_dict import RangeKeyDict

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
```
