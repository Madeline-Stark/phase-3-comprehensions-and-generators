#!/usr/bin/env python3
# got error with pytest -x, had to jsut run pytest

def return_evens(num_list):
    # returns a list of all of the even elements of a sequence of integers.
   return [n for n in num_list if n % 2 == 0]
   

def make_exclamation(sentence_list):
    # takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.
    return [s + "!" for s in sentence_list]
    pass