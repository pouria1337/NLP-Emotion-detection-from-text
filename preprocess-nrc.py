# filter out emotions not mutual with isear_databanl
# export to a new .csv file

# import
import pandas as pd
import os

# function definitions
def get_unique_emotion(isear_databank, nrc_list):
    '''return a set of strings of unique emotions between isear & nrc'''
    return set(nrc_list["Emotion"].unique()).intersection(
        set(isear_databank["Field1"].unique())
        )

def rm_unmutual_words(unique_emos, org_dataframe):
    '''
    remove from the NRC list word the emotion of which is absent
    in isear databank.
    return the resulting dataframe of processed nrc words 
    '''
    org_dataframe = org_dataframe[org_dataframe["Emotion"].isin(unique_emos)]       # isin() function returns a list of 0s and 1s corresponding to satisfied criteria
    return org_dataframe.reset_index(drop = True)


def rm_non_member_words(org_dataframe):
    '''
    Each word is listed for every emotion. Its connection is denoted by
    the "Member" column of the word being 1 or 0
    Remove words the Member column of which are 0
    '''
    org_dataframe = org_dataframe[org_dataframe["Member"] == 1]
    return org_dataframe.reset_index(drop = True)


def export_to_csv(org_dataframe):
    if (not(os.path.exists("./cleaned-data"))):
        os.makedirs("./cleaned-data")

    org_dataframe.to_csv("./cleaned-data/clean_nrc_list.csv", 
                         index = False, 
                         columns = ["Word", "Emotion"])

if __name__ == "__main__":
    print("Processing unique emotions...", end = '')
    isear_databank = pd.read_csv("./data/isear_databank.csv", 
                                 encoding = "latin-1", 
                                 usecols = ["Field1", "SIT"])                       # read isear_databank into a dataframe
    
    nrc_list = pd.read_csv("./data/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt",
                           encoding= 'unicode-escape', 
                           sep="\t", 
                           names = ['Word', 'Emotion', 'Member'])                   # read NRC-Emotion-Lexicon-Wordlevel-v0.92 file into a dataframe & give it column names
    print(" Complete.\n")

    print("Size of the NRC word list before removing unmutual emotions: {}"
          .format(nrc_list.shape[0]))
    nrc_list = rm_unmutual_words(get_unique_emotion(isear_databank, nrc_list),      # remove words the emotions of which are absent in the isear databank
                                 nrc_list)
    print("Size of the NRC word list after removing unmutual emotions: {}\n"
          .format(nrc_list.shape[0]))

    print("Attempting to remove non-member words...", end = "")
    nrc_list = rm_non_member_words(nrc_list)                                        # remove non-member words
    print(" Complete.")
    print("Size of the NRC word list after removing non-member words: {}\n"
          .format(nrc_list.shape[0]))
    
    print("Exporting the cleaned NRC word list to .csv...", end = "")
    export_to_csv(nrc_list)                                                         # exporting the nrc list to a .csv file keeping only the "Word" & "Emotion" columns
    print("Complete.")