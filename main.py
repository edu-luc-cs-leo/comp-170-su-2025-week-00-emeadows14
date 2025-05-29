#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name is invalid because begins with a number instead of a letter.
3. age is valid because it uses all letters and is not a reserved string.
4. total_amount is valid because it uses letters and is in snake case.
5. while is invalid because it is a reserved string for statements.
6. Student is a valid name because it uses all letters.
7. my-variable is an invalid name because it does not use a '_' as a space between words.
8. for is invalid because it is a reserved string for statements.
9. _temp is valid, but it is not conventional to use underscores at the beginning of a name.
10. value# is invalid because it uses a character other than alphanumeric characters or underscores.


"""
# Problem 2
"""
1. calculate_total is valid
2. 3rd_function is not valid because it starts with a number and function names can only start with letters or underscores.
3. print_values is valid
4. find-item is not valid because it does not use an underscore as spaces between words.
5. def is not valid because it is a reserved string for function statements
6. updateProfile is valid
7. my_function is valid
8. try is valid
9. init_data
10. value@function is not valid because it uses characters that are not numbers, letters, or underscores


"""
# Problem 3
"""
1. the expression is not valid because both sides of the boolean operator and must be equivalent truth values, which true and false are not
2. invalid, 
3. invalid, 
4. valid
5. invalid
6. valid
7. valid
8. valid
9. invalid
10. invalid 


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
