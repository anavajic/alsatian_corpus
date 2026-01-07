import als_retrieve_1
import difflib
x = "Flora"
y = "Flora"
print(difflib.SequenceMatcher(None, x.lower(), y.lower()).ratio())
