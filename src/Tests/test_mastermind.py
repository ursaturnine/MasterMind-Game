"""Functional Unittests with Pytest
- Test Coverage By Function
"""


import pytest
from src.API.randomGenerator import generateNumber
from src.Components.MasterMind import MasterMind
from src.Components.ChatBot import ChatBot
from src.Components.Computer import Computer


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


def test_formatted_response_digits_each_lt_or_equal_to_seven():

    formatted_response = generateNumber()

    chars = []

    for char in formatted_response:
        chars.append(char)
    
    while chars:
        num = chars.pop()

    assert int(num) <= 7

def test_formatted_response_digits_gt_or_equal_to_zero():
    formatted_response = generateNumber()

    chars = []

    for char in formatted_response:
        chars.append(char)
    
    while chars:
        num = chars.pop()

    assert int(num) >= 0

#========================================================COMPUTER TESTS=================================================================
def test_number_dict_has_length_four():
    c = Computer()

    c.randomNumber = '1234'

    c_dict = c.ansToDict()

    assert len(c_dict) == 4

def test_number_dict_is_type_dict():
    c = Computer()

    c.randomNumber = '1234'

    c_dict = c.ansToDict()

    assert type(c_dict) == dict

def test_keys_in_dict_are_strings():
    c = Computer()

    c.randomNumber = '1234'

    c_dict = c.ansToDict()
    for key in c_dict:
        assert type(key) == str


def test_number_dict_values_are_type_list():
    c = Computer()

    c.randomNumber = '1234'

    c_dict = c.ansToDict()

    assert type(c_dict['1']) == list
    assert type(c_dict['2']) == list
    assert type(c_dict['3']) == list
    assert type(c_dict['4']) == list

# ========================================================MATCHNUM() TESTS==============================================================

def test_matchNums_three_correct_nums_and_three_correct_consecutive_places_returns_three():

    m = MasterMind()

    guess = '1235'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 3

def test_matchNums_four_correct_nums_and_zero_correct_places_returns_four():

    m = MasterMind()


    guess = '4321'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }

    correct = m.matchNums(guess, num)

    assert correct == 4

def test_matchNums_zero_correct_nums_returns_zero():
    m = MasterMind()


    guess = '9999'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }

    correct = m.matchNums(guess, num)

    assert correct == 0

def test_matchNums_three_non_consecutive_correct_nums_returns_three():
    m = MasterMind()

    guess = '1254'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 3


def test_matchNums_one_correct_num_at_start_of_num_duplicated_returns_one():
    m = MasterMind()

    guess = '1111'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 1

def test_matchNums_one_correct_num_at_end_of_num_duplicated_returns_one():
    m = MasterMind()

    guess = '4444'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 1

def test_matchNums_one_correct_nums_duplicated_in_middle_of_num_returns_one():
    m = MasterMind()

    guess = '5225'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 1

def test_four_correct_nums_returns_four():
    m = MasterMind()

    guess = '1234'

    num = {
        '1': [0, 1],
        '2': [1, 1],
        '3': [2, 1],
        '4': [3, 1]
    }


    correct = m.matchNums(guess, num)

    assert correct == 4

#===============================================MATCHLOCS() TESTS========================================================

def test_three_consecutive_correct_locations_returns_three():

    m = MasterMind()

    guess = '1237'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 3

def test_three_non_consecutive_correct_locations_returns_three():

    m = MasterMind()

    guess = '1274'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 3


def test_one_correct_location_four_correct_numbers_returns_one():
    m = MasterMind()

    guess = '1423'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 1


def test_four_correct_locations_returns_four():
    m = MasterMind()

    guess = '1234'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 4

def test_one_correct_location_duplicated_at_start_of_num_returns_one():
    m = MasterMind()

    guess = '1100'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 1

def test_one_correct_location_duplicated_at_end_of_num_returns_one():
    m = MasterMind()

    guess = '0044'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 1


def test_zero_correct_locations_returns_zero():
    m = MasterMind()

    guess = '8888'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 0

def test_two_consecutive_correct_locations_returns_two():
    m = MasterMind()

    guess = '1288'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 2

def test_two_non_consecutive_correct_locations_returns_two():
    m = MasterMind()

    guess = '1884'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 2

def test_two_alternating_correct_locations_returns_two():
    m = MasterMind()

    guess = '1838'

    num = {
        '1': [(0,), 1],
        '2': [(1,), 1],
        '3': [(2,), 1],
        '4': [(3,), 1]
    }

    correct = m.matchLocs(guess, num)

    assert correct == 2


# ==========================================CHATBOT TESTS==========================================================

def test_four_correct_nums_four_correct_places_returns_four_and_four_respectively():
    
    b = ChatBot()

    correctNums = 4
    correctLocs = 4

    comms = b.guess_summary(correctNums, correctLocs)

    assert comms == "4 correct numbers and 4 correct locations"


def test_four_correct_nums_zero_correct_places_returns_four_and_zero_respectively():
    b = ChatBot()

    correctNums = 4
    correctLocs = 0

    comms = b.guess_summary(correctNums, correctLocs)

    assert comms == "4 correct numbers and 0 correct locations"

def test_one_correct_num_and_one_correct_place_returns_one_and_one_respectively():
    b = ChatBot()

    correctNums = 1
    correctLocs = 1

    comms = b.guess_summary(correctNums, correctLocs)

    assert comms == "1 correct numbers and 1 correct locations"

    



