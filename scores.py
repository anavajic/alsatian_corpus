
import phonetics
import pandas as pd
import difflib

def add_pronunciation(data: pd.DataFrame) -> pd.DataFrame:
  """
  Adds pronunciations of German, French, and Alsatian words using the Double Metaphone algorithm.
  :param data: A pandas DataFrame containing columns 'German', 'Alsatian', and 'French' with text data.
  :return: The input DataFrame with added columns 'germ_pron', 'als_pron', and 'fr_pron' containing the Double Metaphone phonetic representations of the respective language text.
  """
  data["germ_pron"] = data["German"].apply(phonetics.dmetaphone)
  data["als_pron"] = data["Alsatian"].apply(phonetics.dmetaphone)
  data["fr_pron"] = data["French"].apply(phonetics.dmetaphone)
  return data


def orth_score(x: str, y: str) -> float | str:
  """
  Calculates the string similarity score between two words using the difflib.SequenceMatcher.ratio() function if a given French or German word has an Alsatian translation assigned
  :param x: The first string to be compared. Should be a non-period string for valid comparison.
  :param y: The second string to be compared. Should be a non-period string for valid comparison.
  :return: A similarity ratio between the two strings as a float if both are non-period strings. Returns a period (".") if either of the inputs is a period string.
  """
  if isinstance(x, str) and len(x) > 0 and isinstance(y, str) and len(y) > 0:
    if x != "." and y != ".":
      return difflib.SequenceMatcher(None, x.lower(), y.lower()).ratio()
    return "."
  else:
    raise ValueError("Invalid input")

def pron_score(x: tuple[str, str], y: tuple[str, str]) -> float | str:
  """
  Calculates the string similarity score between two pronunciations using the difflib.SequenceMatcher.ratio() function if a given French or German word has an Alsatian translation assigned
  :param x: A tuple containing two string elements. The first element represents the primary string, and the second element represents the optional string for comparison.
  :param y: A tuple containing two string elements. The first element represents the primary string, and the second element represents the optional string for comparison.
  :return: The highest similarity score as a float between the string elements of the tuples x and y based on sequence matching. Returns a string "." if both tuples contain empty strings (i.e. if the word has no Alsatian translation assigned)
  """
  if x != ('', '') and y != ('', ''):
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
  return "."



