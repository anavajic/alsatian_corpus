import pandas as pd
import als_retrieve_2_1

def tr_retrieve(word: str, tr: list) -> bool:
    """
    Checks a list of words for matches with a given word (match indicates that the Alsatian column can be considered a translation of the given word)
    :param word: French or German word
    :param tr: A list containing French or German words
    :return: Boolean value indicating whether the word exists in the list.
    """
    if word in tr:
        return True
    return False

def match_search(data: pd.DataFrame) -> pd.DataFrame:
    """
    Iterates through French-German dictionary spreadsheet and adds Alsatian translations by searching for matches in the French-German-Alsatian spreadsheet.
    :param data: pandas DataFrame containing "German" and "French" columns, representing German and French text data respectively.
    :return: pandas DataFrame with an additional column "Alsatian", containing Alsatian translations derived from the French-German-Alsatian spreadsheet.
    """
    alsatian_dict = pd.read_excel("alsatian-alignments.xlsx")
    data["Alsatian"] = "."

    for i in range(len(data)):
        for j in range(len(alsatian_dict)):
            wg = data.loc[i]["German"].lower()
            tg = alsatian_dict.loc[j]["German"].lower().split(";")
            wf = data.loc[i]["French"].lower()
            tf = alsatian_dict.loc[j]["French"].lower().split(";")

            if tr_retrieve(wg, tg):
                data.loc[i,"Alsatian"] = als_retrieve_2_1.clean(alsatian_dict.loc[j]["Alsatian"]).split(";")[0]
            elif tr_retrieve(wf, tf):
                data.loc[i,"Alsatian"] = als_retrieve_2_1.clean(alsatian_dict.loc[j]["Alsatian"]).split(";")[0]
    return data



