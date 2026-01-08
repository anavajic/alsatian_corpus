"""
Adds Alsatian translations to the French-German dictionary spreadsheet,
generates pronunciations using the Double Metaphone algorithm
and calculates string similarity scores
between French-Alsatian and German-Alsatian word pairs, as well as between their respective pronunciations.
"""
import pandas as pd
import dictionary_lookup
import scores


if __name__ == "__main__":
    dataset = pd.read_csv("german-french.csv")

    dataset = dictionary_lookup.match_search(dataset)
    dataset = scores.add_pronunciation(dataset)

    dataset["orth_score_germ_als"] = dataset.apply(lambda x: scores.orth_score(x.German, x.Alsatian), axis=1)
    dataset["orth_score_fr_als"] = dataset.apply(lambda x: scores.orth_score(x.French, x.Alsatian), axis=1)
    dataset["pron_score_fr_als"] = dataset.apply(lambda x: scores.pron_score(x.fr_pron, x.als_pron), axis=1)
    dataset["pron_score_germ_als"] = dataset.apply(lambda x: scores.pron_score(x.germ_pron, x.als_pron), axis=1)

    print(dataset.head(100))
    dataset.to_csv("dataset_with_scores.csv")