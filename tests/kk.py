import als_retrieve_1
import difflib
pron1 = ('AFRNT', '')
pron2 = ('PLTKNK', '')
print(difflib.SequenceMatcher(None, pron1[0].lower(), pron2[0].lower()).ratio())
