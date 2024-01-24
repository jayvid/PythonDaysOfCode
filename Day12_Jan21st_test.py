import pytest
from Day12_Jan21st import reverse_string

test_data = {
    '1': ('',''),                           # scenario 1 : string with no characters
    '2': ('a', 'a'),                        # scenario 2 : string with single character
    '3': ('hello', 'olleh'),                # scenario 3 : string with alphabets
    '4' : ('Hello World','dlroW olleH'),    # scenario 4 : string with space separated words
    '5' : ('#hEll0@','@0llEh#'),            # scenario 5 : string with alphabets, numbers and special characters
    '6' : ('$%#@^)',')^@#%$'),              # scenario 6 : string with only special characters
    '7' : (1, "Incorrect datatype"),        # scenario 7 : integer
    '8' : ([1,2], "Incorrect datatype")     # scenario 8 : list
}

@pytest.mark.parametrize("test_data", test_data.values())
def test_reverse_string(test_data):
    assert reverse_string(test_data[0]) == test_data[1]