import typing

'''
This module handles text parsing and tokenization.
'''

def tokenize(string:str):
    return string.strip(',.;?!').split()

@spec parse
def parse():
    