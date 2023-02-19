import pytest
from randomGenerator import generateNumber
from master_mind import ansToDict


# ================================================API TESTS========================================================

def test_random_generator_API_returns_string():
    num = generateNumber()


    assert type(num) == str


def test_length_of_formatted_response_is_four():
    

    formatted_response = generateNumber()


    assert len(formatted_response) == 4

def test_formatted_response_string_contains_numbers():

    formatted_response = generateNumber()

    assert formatted_response.isdigit()


def test_formatted_response_digits_each_lt_seven():

    formatted_response = generateNumber()

    chars = []

    for char in formatted_response:
        chars.append(char)
    
    while chars:
        num = chars.pop()

    assert int(num) < 7

def test_formatted_response_digits_gt_zero():
    formatted_response = generateNumber()

    chars = []

    for char in formatted_response:
        chars.append(char)
    
    while chars:
        num = chars.pop()

    assert int(num) > 0

# =======================================GAME PLAY TESTS========================================================

@pytest.skip
def test_answer_formatted_to_dictionary():

    num = '1234'

    answer = ansToDict(num)

    assert type(answer) == dict

@pytest.skip
def test_answer_dict_has_four_keys():

    answer = ansToDict(answer)

    assert len(answer) == 4

@pytest.skip
def test_answer_keys_are_strings():

    num = '1234'

    answer = ansToDict(num)
    assert type(answer.keys() == str)

@pytest.skip
def test_answer_dict_values_are_lists():

    num = '1234'

    answer = ansToDict(num)

    assert type(answer.values() == list)

@pytest.skip
def test_answer_dict_values_has_length_of_two():

    num = '1234'

    answer = ansToDict(num)

    assert len(answer.values() == 2)


    





# test answer is dictionary with 4 keys which are strings and 
# values are lists with 2 items. 


