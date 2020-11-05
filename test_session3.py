import math
from functools import reduce
import random
import string
from functools import partial
import session3
import pytest
import re
import math
import os
import inspect
import unittest

README_CONTENT_CHECK_FOR = ["lambda","reduce","partial","list comprehension","map","zip","filter"]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session3, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_fibonnaci_positive():
    assert True== session3.is_fibonnaci(2), "Fibonnaci function not working proper"

def test_fibonnaci_negative():
    assert False== session3.is_fibonnaci(123435),"passed number is not a Fibonnaci"

def test_evenodd_sum_1():
    l1 = [1,2,3,4]
    l2 = [1,2,3,4]
    assert []== session3.evenodd_sum(l1,l2)


def test_evenodd_sum_2():
    l1 = [1,2,3,4]
    l2 = [3,5,7,8]
    assert [7]== session3.evenodd_sum(l1,l2)

def test_vowel_removal():
    l1 = [1,2,3,4]
    l2 = [3,5,7,8]
    assert 'whtspp'== session3.vowel_removal("whatsapp")

def test_relu_1():
    relu_list = [12,1,1.00,2,-5,8,-23.00,78]
    assert [12, 1, 1.0, 2, 0, 8, 0, 78] == session3.relu(relu_list)

def test_sigmoid_2():
    list1 = [1.51,1.71,-6.36]
    assert [0.819061206847858,0.8468362842349139,0.0017263811657371527] == session3.sigmoid(list1)


def test_magic_shifting():
    assert 'abcde' == session3.magic_shifting('vwxyz')

def test_foul_words_detector_positive():
    text = """In comparison, the second and third most popular swearwords – 
    "shit" and ass – accounted for 15.0% and 14.5% respectively, 
    while other highlights included "bitch" (10.3%), "hell" (4.5%), "whore" (1.8%),
    "dick" (1.7%), "piss" (1.5%) and "pussy" (1.2%)"""
    assert True == session3.foul_words_detector(text)

def test_foul_words_detector_negative():
    text = """In comparison, the second and third most popular swearwords – """
    assert False == session3.foul_words_detector(text)

def test_even_number_sum():
    li = [5, 8, 10, 21, 50, 99] 
    assert 68 == session3.even_number_sum(li)

def test_biggest_accii_char():
    li = 'TSAItsai'
    assert 't' == session3.biggest_accii_char(li)
    
def test_correct_numberplate():
    assert  bool(re.match(r"^[A-Z]{2}\d{2}\D{2}\d{4}$",session3.numberplate()[0]))
    
def test_partial_function():
    assert  bool(re.match(r"^[A-Z]{2}\d{2}\D{2}\d{4}$",session7.veh_number(state='DL')[0]))
    
class vehicle_number(unittest.TestCase):
   def test_partial_function_negative(self):
      self.assertRaises(TypeError, session3.veh_number, 2000, 5000)

if __name__ == '__main__':
   unittest.main()

def test_sum_thirdplaces():
    li = [5, 8, 1, 21, 50, 99, 21, 45, 5, 68, 23] 
    assert 105 == session3.sum_thirdplaces(li)
