
import phonetics
import pandas as pd
import difflib

def add_pronunciation(data):
    data["germ_pron"] = data["German"].apply(phonetics.dmetaphone)
    data["als_pron"] = data["Alsatian"].apply(phonetics.dmetaphone)
    data["fr_pron"] = data["French"].apply(phonetics.dmetaphone)
    return data

def orth_score(x, y):
  return difflib.SequenceMatcher(None, x.lower(), y.lower()).ratio()

def pron_score(x, y):
  #dodati provjeru da ne prolazi ako je tocka
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



