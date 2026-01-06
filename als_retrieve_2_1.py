import pandas as pd
import re

def clean(w: str) -> str:
    """
    Extracts a list of Alsatian words separated by semicolon by removing excess information from the input string
    :param w: Input string (series of Alsatian words) containing irrelevant substrings (codes indicating sources of the words) enclosed in square brackets and excess whitespace.
    :return: A cleaned version of the input string with substrings in square brackets removed, trimmed whitespace, and consistent semicolon separation.
    """
    word = re.compile(r"\[.*?\]")
    w2 = word.sub("", w)
    w3 = w2.split(";")
    w4 = [x.strip() for x in w3]
    w5 = ";".join(w4)
    return w5

