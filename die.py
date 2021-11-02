"""
File: die.py
this module defines the Die class.
"""
from random import randint

class Die(object):

    def __init__(self):
        self._value = 1

    def roll(self):
        self._value = randint(1, 6)

    def getValue(self):
        return self._value

    def __str__(self):
        return  str(self._value)