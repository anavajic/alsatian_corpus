import pandas as pd

def tr_retrieve(word, tr):
    if word in tr:
        return True
    return False

def match_search():
    german_french = pd.read_excel("german-french.ods")
    alsatian_aligned = pd.read_excel("alsatian-alignments.ods")
    german_french["Alsatian"] = "."

    for i in range(len(german_french)):
        for j in range(len(alsatian_aligned)):
            wg = german_french.loc[i]["German"].lower()
            tg = alsatian_aligned.loc[j]["German"].lower().split(";")
            wf = german_french.loc[i]["French"].lower()
            tf = alsatian_aligned.loc[j]["French"].lower().split(";")

            if tr_retrieve(wg, tg):
                german_french.loc[i,"Alsatian"] = alsatian_aligned.loc[j]["Alsatian"]
            if tr_retrieve(wf, tf):
                german_french.loc[i,"Alsatian"] = alsatian_aligned.loc[j]["Alsatian"]

