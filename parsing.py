import typing

'''
This module handles text parsing and tokenization.
Idea: to parse a sentence, have a function that uses currying to assemble a lambda which will execute the command?
'''
# WORD LISTS
UNIMPORTANT_WORDS = ['the', 'a', 'my']

def clean_text(text:str):
    for word in UNIMPORTANT_WORDS:
        text = text.replace(word, "")
    return text

def simple_parse(text:str) -> tuple[str, str, str] | tuple[str, str] | tuple[str]:
    '''
    Takes a simple command:
    <VERB> <DOBJ> (with <IOBJ>)
    
    returns a tuple of either: 
    (verb, dobj, iobj),
    (verb, dobj),
    or (verb).
    '''
    articles = [
        'a ',
        'the ',
    ]
    text = text.lower()
    for fluff in articles:
        text = text.replace(fluff, '')
    verb = text.split()[0]
    if len(text.split()) == 1:
        return (verb)
    nouns = text.replace(verb, '')\
    .strip()\
    .split('with')
    dobj = nouns.pop(0).strip()
    iobj = None
    if len(nouns):
        iobj = nouns.pop(0).strip()
    
    return (verb, dobj, iobj)

# print(
#     simple_parse("attack the orc with the rusty sword")
# )
# print(
#     simple_parse("attack the orc")
# )