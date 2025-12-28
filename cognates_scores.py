
#! pip install phonetics

import phonetics
import pandas as pd
import difflib

dataset = pd.read_excel("german_french.ods")


def add_pronunciation:
    dataset["de_pron"] = dataset["German"].apply(phonetics.dmetaphone)
    dataset["als_pron"] = dataset["Alsatian"].apply(phonetics.dmetaphone)
    dataset["fr_pron"] = dataset["French"].apply(phonetics.dmetaphone)
    

def orth_score(x, y):
  return difflib.SequenceMatcher(None, x.lower(), y.lower()).ratio()

def pron_score(x, y):
  scores = []
  s1 = difflib.SequenceMatcher(None, x[0].lower(), y[0].lower()).ratio()
  scores.append(s1)
  if x[1] is not None and x[1] != "":
    if y[1] is not None:
      s2 = difflib.SequenceMatcher(None, x[0].lower(), y[1].lower()).ratio()
      s3 = difflib.SequenceMatcher(None, x[1].lower(), y[0].lower()).ratio()
      s4 = difflib.SequenceMatcher(None, x[1].lower(), y[1].lower()).ratio()
      scores.append(s2)
      scores.append(s3)
      scores.append(s4)
    else:
      s2 = difflib.SequenceMatcher(None, x[1].lower(), y[0].lower()).ratio()
      scores.append(s2)
  elif y[1] is not None:
    s2 = difflib.SequenceMatcher(None, x[0].lower(), y[1].lower()).ratio()
    scores.append(s2)
  return max(scores)

#https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe

fr["orth_score"] = fr.apply(lambda x: orth_score(x.French, x.Alsatian), axis=1)
de["orth_score"] = de.apply(lambda x: orth_score(x.German, x.Alsatian), axis=1)
fr["pron_score"] = fr.apply(lambda x: pron_score(x.fr_pron, x.als_pron), axis=1)
de["pron_score"] = de.apply(lambda x: pron_score(x.de_pron, x.als_pron), axis=1)

de.head()

de.to_excel("DE_FINAL_SCORES.xlsx")
fr.to_excel("FR_FINAL_SCORES.xlsx")