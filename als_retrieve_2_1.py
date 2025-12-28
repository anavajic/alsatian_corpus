import pandas as pd
import re

def clean(w):
    mot = re.compile(r"\[.*?\]")
    w2 = mot.sub("", w)
    w3 = w2.split(";")
    w4 = [x.strip() for x in w3]
    w5 = ";".join(w4)
    return w5

