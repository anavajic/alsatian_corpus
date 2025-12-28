import pandas as pd
from als_retrieve_1 import  tr_retrieve, match_search
from als_retrieve_2_1 import clean
from cognates_scores import add_pronunciation, orth_score, pron_score


match_search()
add_pronunciation()

dataset["orth_score"] = dataset.apply(lambda x: orth_score(x.German, x.Alsatian), axis=1)
dataset["pron_score"] = dataset.apply(lambda x: pron_score(x.fr_pron, x.als_pron), axis=1)