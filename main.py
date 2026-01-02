import pandas as pd
from als_retrieve_1 import match_search
from cognates_scores import add_pronunciation, orth_score, pron_score


if __name__ == "__main__":
    dataset = pd.read_csv("german-french.csv")

    dataset = match_search(dataset)
    dataset = add_pronunciation(dataset)

    dataset["orth_score_germ_als"] = dataset.apply(lambda x: orth_score(x.German, x.Alsatian), axis=1)
    dataset["orth_score_fr_als"] = dataset.apply(lambda x: orth_score(x.French, x.Alsatian), axis=1)
    dataset["pron_score_fr_als"] = dataset.apply(lambda x: pron_score(x.fr_pron, x.als_pron), axis=1)
    dataset["pron_score_germ_als"] = dataset.apply(lambda x: pron_score(x.germ_pron, x.als_pron), axis=1)

    print(dataset.head(100))
    dataset.to_csv("dataset_with_scores.csv")