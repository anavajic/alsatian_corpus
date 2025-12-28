import pandas as pd

def tr_retrieve(word, tr):
    if word in tr:
        return True
    return False

def match_search():
    dataset = pd.read_excel("german-french.ods")
    alsatian_dict = pd.read_excel("alsatian-alignments.ods")
    dataset["Alsatian"] = "."

    for i in range(len(dataset)):
        for j in range(len(alsatian_dict)):
            wg = dataset.loc[i]["German"].lower()
            tg = alsatian_dict.loc[j]["German"].lower().split(";")
            wf = dataset.loc[i]["French"].lower()
            tf = alsatian_dict.loc[j]["French"].lower().split(";")

            if tr_retrieve(wg, tg):
                dataset.loc[i,"Alsatian"] = alsatian_dict.loc[j]["Alsatian"]
            if tr_retrieve(wf, tf):
                dataset.loc[i,"Alsatian"] = alsatian_dict.loc[j]["Alsatian"]
    return dataset



