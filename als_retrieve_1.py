import pandas as pd

def tr_retrieve(word, tr):
    if word in tr:
        return True
    return False

def match_search():
    dataset = pd.read_excel("german-french.ods")
    alsatian_aligned = pd.read_excel("alsatian-alignments.ods")
    dataset["Alsatian"] = "."

    for i in range(len(dataset)):
        for j in range(len(alsatian_aligned)):
            wg = dataset.loc[i]["German"].lower()
            tg = alsatian_aligned.loc[j]["German"].lower().split(";")
            wf = dataset.loc[i]["French"].lower()
            tf = alsatian_aligned.loc[j]["French"].lower().split(";")

            if tr_retrieve(wg, tg):
                dataset.loc[i,"Alsatian"] = alsatian_aligned.loc[j]["Alsatian"]
            if tr_retrieve(wf, tf):
                dataset.loc[i,"Alsatian"] = alsatian_aligned.loc[j]["Alsatian"]



