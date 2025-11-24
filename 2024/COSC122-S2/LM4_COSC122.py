#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 23:19:05 2024

@author: seanfaulkner
"""
import re
import os
from time import perf_counter
import doctest
from spelling import QuadraticHashTable

# setup a ruled line string
LINE_WIDTH = 50
SINGLE_LINE = '-' * LINE_WIDTH

def print_line():
    """ Prints a single line """
    print(SINGLE_LINE)


def _c_mul(value_a, value_b):
    '''Substitute for c multiply function'''
    return ((int(value_a) * int(value_b)) & 0xFFFFFFFF)


def nice_hash(input_string):
    '''Takes a string name and returns a hash for the string. This hash value
    will be os independent, unlike the default Python hash function.'''
    if input_string is None:
        return 0  # empty
    value = ord(input_string[0]) << 7
    for char in input_string:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(input_string)
    if value == -1:
        value = -2
    return value
print(nice_hash('Zoe'))
print(149707909%11)
print(3013802077%5)

hash_table = QuadraticHashTable(7)
hash_table.store('Jim')
hash_table.store('Aby')
hash_table.store('Ken')
hash_table.store('Bob')
hash_table.store('Art')
hash_table.store('Jon')
print(hash_table)