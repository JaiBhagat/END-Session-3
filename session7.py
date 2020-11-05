import math
from functools import reduce
import random
import string
from functools import partial
import numpy as np

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
fibonnaci_list = fib(10000)

def is_fibonnaci(x):
    '''This method can be used when we dont have a list of fibonnaci number '''
    return bool(list(filter(lambda x : x in fibonnaci_list,[x])))
def evenodd_sum(list1,list2):
    ''' add 2 iterables a and b such that a is even and b is odd '''
    return [a + b for a, b in zip(list1, list2) if a % 2==0 and b % 2 != 0 ]
def vowel_removal(text):
    '''strips every vowel from a string provided (tsai>>t s) '''
    return "".join([x for x in text if x not in ['a','e','i','o','u']])
def relu(relu_list):
    ''' acts like a ReLU function for a 1D array '''
    return [0 if x < 0 else x for x in relu_list]
def sigmoid(list1):
    ''' #acts like a sigmoid function for a 1D array '''
    sigmoid_list = [1/(1 + np.exp(-x)) for x in list1]
    return sigmoid_list
def magic_shifting(text):
    ''' #takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn '''
    return "".join([chr((ord(x)+5)) if ord(x)>122 else chr((ord(x)+5)-26) for x in text])    
def foul_words_detector(text):
    '''  A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt '''
    f = open("swear_list.txt", "r")
    swear_list = [l.rstrip() for l in f.readlines()]
    return bool([r for r in text.split(" ") if any(z in r for z in swear_list)])
def even_number_sum(l):
    ''' Using reduce function:add only even numbers in a list '''
    return reduce((lambda x, y: x + y), [x for x in l if x%2==0])
def biggest_accii_char(l):
    ''' Using reduce function:find the biggest character in a string (printable ascii characters) '''
    return reduce(lambda x, y: x if ord(x)>ord(y) else y,l)
def sum_thirdplaces(l):
    ''' Using reduce function:adds every 3rd number in a list '''
    return reduce((lambda x, y: x + y), [x for ind, x in enumerate(l) if ind == 2 or ind % 3 == 2])
def numberplate():
    ''' Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number 
    plates,where KA is fixed, D stands for a digit, and A stands for Capital alphabets.10<<DD<<99 & 1000<<DDDD<<9999 '''
    return ['KA'+(str(random.randint(10,99))+random.choice(string.ascii_uppercase)+
    random.choice(string.ascii_uppercase)+str(random.randint(1000,9999))) for item in range(15)]
def numberplate_v1(r1,r2,state = 'KA'):
    ''' This fucntion is a helper fucntion to the patial fucntion which gives user to change the state value and generate random number plates '''
    return [state+(str(random.randint(10,99))+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+str(random.randint(r1,r2))) for item in range(15)]    
veh_number = partial(numberplate_v1,r1=1000,r2=9999)
