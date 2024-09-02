# preprocess isear data from .csv form 
# remove columns whose emotions do not correspond to NRC

# import
import pandas as pd
import os       # to handle exporting to a .csv in a new directory


# function definitions
def get_unique_emotion(isear_databank, nrc_list):
    '''return a set of strings of unique emotions between isear & nrc'''
    return set(nrc_list["Emotion"].unique()).intersection(set(isear_databank["Field1"].unique()))

def filter_for_emotion(unique_emos, isear_databank):
    '''removes rows from the isear databank dataframe that do not have an emotion in the unique emotion list
       returns the cleaned dataframe
    '''

    # only include rows of which the emotion column is a member of unique emotions
    isear_databank = isear_databank[isear_databank["Field1"].isin(unique_emos)]
    # reset the index number column to correspond to the number of rows
    return isear_databank.reset_index(drop = True)

def rm_invalid_rows(org_dataframe):
    '''
       some rows include "Blank." or "No Response.", "[ No description.]", "[ Never experienced.]", "NO RESPONSE"
       remove such rows from the dataframe
       remove the á character
    '''

    # remove invalid responses
    # first value is the number of occurances, second member is the the list of row numbers
    remove_vals = {
        "Blank.": [0, []],
        "No Response.": [0, []], 
        "[ No description.]": [0, []], 
        "[ Never experienced.]": [0, []], 
        "NO RESPONSE": [0, []],
        "[ Can not remember.]": [0, []],
        "[ Can not think of any situation.]": [0, []]
        }
    # keep track of the row number
    row_number = 0
    for memory in org_dataframe["SIT"]:
        if (memory == "Blank." 
            or memory == "No Response." 
            or memory == "[ No description.]" 
            or memory == "[ Never experienced.]" 
            or memory == "NO RESPONSE"
            or memory == "[ Can not remember.]"
            or memory == "[ Can not think of any situation.]"):
            remove_vals[memory][0] += 1
            remove_vals[memory][1].append(row_number)
        row_number += 1

    # remove rows according the remove_vals dictionary
    for key, value in remove_vals.items():
        # choose an element that exists in the isear databank dataframe
        if remove_vals[key][0] > 0:    # if the first value of a key, which signifies its presence in dataframe, is above 0
            org_dataframe.drop(remove_vals[key][1], axis = 0, inplace = True)       # the remove_vals[key][1] expression evaluates to a list so it's plug & play

    # reset index to allow subscription into the dataframe
    org_dataframe.reset_index(drop = True, inplace = True)

    # remove the invalid character á
    # loop over each row, if á is present replace it with an empty substring ''
    for row_n in range(0, org_dataframe.shape[0]):
        if "á" in org_dataframe.loc[row_n, "SIT"]:
            org_dataframe.loc[row_n, "SIT"] = org_dataframe.loc[row_n, "SIT"].replace("á", "")         
        
    return org_dataframe.reset_index(drop = True)


def export_to_csv(org_dataframe):
    if (not(os.path.exists("./cleaned-data"))):
        os.makedirs("./cleaned-data")

    org_dataframe.to_csv("./cleaned-data/clean_isear_databank.csv", index = False)
        

# akin to the main() function in C & C++
if (__name__) == "__main__":
    # read isear_databank into a dataframe
    print("Processing unique emotions...", end = '')
    isear_databank = pd.read_csv("./data/isear_databank.csv", encoding = "latin-1", usecols = ["Field1", "SIT"])
    # read NRC-Emotion-Lexicon-Wordlevel-v0.92 file into a dataframe & give it column names
    nrc_list = pd.read_csv("./data/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", encoding= 'unicode-escape', sep="\t", names = ['Word', 'Emotion', 'Member'])
    print(" Complete")

    print("Isear databank size before removing unsupported emotions: {}\n".format(isear_databank.shape[0]))

    print("Attempting to remove rows emotion of which is not mutual with NRC...", end = '')
    isear_databank = filter_for_emotion(get_unique_emotion(isear_databank, nrc_list), isear_databank)
    print(" Complete.")
    print("Isear databank size after removing unsupported emotions: {}\n".format(isear_databank.shape[0]))

    print("Attempting to remove rows with the invalid character \"á\", and invalid responses...", end = "")
    isear_databank = rm_invalid_rows(isear_databank)
    print(" Complete.")
    print("Isear databank size after removing invalid rows and the \"á\" character: {}\n".format(isear_databank.shape[0]))

    print("Exporting to .csv...", end = "")
    export_to_csv(isear_databank)
    print(" Complete.")
