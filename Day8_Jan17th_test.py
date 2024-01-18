from Day8_Jan17th import string_upper_lower_count
import pytest

"""
Test scenarios
scenario 1 : empty string
scenario 2 : no upper or lower cases so both counts should be zero
scenario 3 : only upper case letters - single word
scenario 4 : only upper case letters - multiple words
scenario 5 : only lower case letters - single word
scenario 6 : only lower case letters - multiple words
scenario 7 : string with special characters and some uppercase/lowercase letters - single word
scenario 8 : string with special characters and some uppercase/lowercase letters - multiple words
scenario 9 : string with only special characters and no uppercase/lowercase letters - single word
scenario 10 : string with only special characters and no uppercase/lowercase letters - multiple word
"""
expected_results = {"":(0,0), "1234":(0,0), "HELLO":(5,0), "HELLO WORLD":(10,0), "hello":(0,5), "hello world":(0,10), 
                    "heLlo%43_wOrld":(2,8), "heLlo%43_wOrld w@tsUp":(3,12), "!@#$%^&*()":(0,0), "!@#$%^&*( !@#$%^&*)_+":(0,0)}

#@pytest.mark.parametrize("test_string",["", "1234"])
@pytest.mark.parametrize("test_string",list(expected_results.keys()))
def test_string_upper_lower_count(test_string):
    assert string_upper_lower_count(test_string) == expected_results[test_string], "Test failed for string {} \
        : Function does not work as expected".format(test_string)