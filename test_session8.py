
import pytest
import random
import string
import session8
import os
import inspect
import re

CONTENT_CHECK = [
    'closure',
    'doc'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def some_function():
    """Summary or Description of the Function
    Parameters:
    argument1 (int): Description of arg1
    Returns:
    int:Returning value
    """

def test_doc_string_outer():
    fn = session8.doc_string_outer()
    assert fn(some_function) == True

def test_fibonacci_number():
    fn = session8.fibo_outer(3)
    assert fn() == 5
    assert fn() == 8
    assert fn() == 13
    assert fn() == 21
    
def add(a, b):
    return a + b
def mul(a, b):
    return a*b
def div (a , b):
    if b !=0:
        return(a/b)
    else:
        return(None)
    
def test_counter():
    counter_add = session8.counter(add)
    counter_mul = session8.counter(mul)
    counter_div = session8.counter(div)
    counter_add(1, 2)
    counter_add(3, 4)
    counter_add(6, 5)
    counter_mul(20,2)
    counter_mul(40,3)
    counter_mul(100,6)
    counter_div(10,2)
    assert session8.counters == {'add' : 3 , 'mul' : 3 , 'div' : 1 }
    counter_mul(100,6)
    counter_div(10,2)
    assert session8.counters == {'add' : 3 , 'mul' : 4 , 'div' : 2 }
    
times_dict1 = {'add' : 0 , 'mul' : 0 , 'div' : 0 }
times_dict2 = {'add' : 0 , 'mul' : 0 , 'div' : 0 }

def test_counter2():   
    counter_times_dict1 = session8.counter_dict(times_dict1)
    counter_times_dict1(add,1, 2)
    counter_times_dict1(add,10, 20)
    counter_times_dict1(mul,1, 2)
    counter_times_dict1(mul,10, 20)
    counter_times_dict1(mul,3, 2)
    counter_times_dict1(div,1, 2)
    counter_times_dict1(div,4, 10)
    counter_times_dict1(div,100, 2)
    assert times_dict1 == {'add' : 2 , 'mul' : 3 , 'div' : 3 }
    
    counter_times_dict2 = session8.counter_dict(times_dict2)
    counter_times_dict2(add,1, 2)
    counter_times_dict2(mul,10, 20)
    counter_times_dict2(mul,1, 2)
    counter_times_dict2(mul,10, 20)
    counter_times_dict2(mul,3, 2)
    counter_times_dict2(mul,1, 2)
    counter_times_dict2(div,4, 10)
    counter_times_dict2(div,100, 2)
    assert times_dict2 == {'add' : 1 , 'mul' : 5 , 'div' : 2 }
