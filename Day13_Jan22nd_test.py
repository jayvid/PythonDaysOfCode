import pytest
from Day13_Jan22nd import shuffle_list

"""
Test scenarios
scenario 1 : empty list
scenario 2 : list with one element
scenario 3 : every shuffle should create a shuffled list
"""
@pytest.mark.parametrize("input_list",[[], [2], [1,2,3],['a','b','c'],[1,'a', {'a':10}]])
def test_list_shuffle(input_list):
    if len(input_list) == 0 or len(input_list) == 1 :
        assert shuffle_list(input_list) == input_list, "List is not correctly shuffled"
    else:
        original_list = input_list.copy()
        first_shuffle = shuffle_list(input_list) 
        assert first_shuffle != original_list, "List is not correctly shuffled"

        second_shuffle = shuffle_list(original_list)
        assert second_shuffle != first_shuffle, "List is not correctly shuffled when shuffled a 2nd time"