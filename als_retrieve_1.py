import pandas as pd
from als_retrieve_2_1 import clean

def tr_retrieve(word, tr):
    if word in tr:
        return True
    return False

def match_search(data):
    alsatian_dict = pd.read_excel("alsatian-alignments.xlsx")
    data["Alsatian"] = "."

    for i in range(len(data)):
        for j in range(len(alsatian_dict)):
            wg = data.loc[i]["German"].lower()
            tg = alsatian_dict.loc[j]["German"].lower().split(";")
            wf = data.loc[i]["French"].lower()
            tf = alsatian_dict.loc[j]["French"].lower().split(";")

            if tr_retrieve(wg, tg):
                data.loc[i,"Alsatian"] = clean(alsatian_dict.loc[j]["Alsatian"])[0]
            elif tr_retrieve(wf, tf):
                data.loc[i,"Alsatian"] = clean(alsatian_dict.loc[j]["Alsatian"])[0]
    return data



