import typing

'''
This module handles text parsing and tokenization.
'''
# WORD LISTS
UNIMPORTANT_WORDS = ['the', 'a', 'my']

def clean_text(text:str):
    for word in UNIMPORTANT_WORDS:
        text = text.replace(word, "")
    return text

def simple_parse(text:str):
    '''
    Takes a simple command:
    <VERB> <DOBJ> (with <IOBJ>)
    '''
    # Split the text into verb+dobject and iobject
    output = [x.split(' ', 1) for x in text.split('with')]