# combine all merged stories from all authors into one dataframe
# remove unnecessary column(s)
# remove rows with useless emotions

# import
import json
import os
import pandas as pd

# global variables
merge_dir = "./merged-data"

def all_into_one():
    '''
    Merge all merged stories from all authors into one dataframe & return it
    '''
    dataframes = [pd.DataFrame(), pd.DataFrame(), pd.DataFrame()]
    # access different dataframes
    i = 0
    # loop over each merged file
    for f in os.listdir(merge_dir):
        # after reading each file into a dataframe, assign it to an element in "dataframes"
        dataframes[i] = (pd.read_csv(merge_dir + "/" + f, names=['SentID:SentID', 'PE', 'Mood', 'Sentence'], sep="\t"))
        i += 1

    # merge all dataframes together
    return pd.concat(dataframes)


def rm_useless_columns(org_dataframe):
    ''' the "SentID:SentID" column is useless for our purposes. 
        remove it.
    '''
    org_dataframe.drop(columns = ["SentID:SentID"], inplace = True)
    return org_dataframe.reset_index(drop = True)


def rm_nn_rows(org_dataframe):
    '''
    remove rows where all emotions of which is N (PE & Mood columns)
    remove rows where the emotion of which is only +, -, Su+, Su-
    '''

    # remove N:N N:N rows
    print("Dataframe holds {} rows before the removal of N:N rows."
          .format(org_dataframe.shape[0]))
    nn_row_list = []
    # loop over the AIO dataframe of stories
    for i in range(0, org_dataframe.shape[0]):
        pe_val = org_dataframe.loc[i, "PE"]
        mood_val = org_dataframe.loc[i, "Mood"]
        if ("N:N" == pe_val and "N:N" == mood_val):
            # record index number to delete the row later
            nn_row_list.append(i)
    print("There are ", len(nn_row_list), " rows with both emotion columns having N:N as value.")
    print("Attempting to remove N:N only rows...", end = "")
    org_dataframe.drop(nn_row_list, axis = 0, inplace = True)                                       # drop N:N N:N detectd rows
    org_dataframe.reset_index(drop = True, inplace = True)                                          # org_dataframe is to be processed again in this function
    print(" Complete.\n")

    print("Dataframe now holds {} rows.\n".format(org_dataframe.shape[0]))
    return org_dataframe


def keep_target_emotions(org_dataframe):
    '''
    Keep A for angry, D for disgusted, F for fearful, H for happy, Sa & S for sad
    Create a dictionary of respective emotion keywords with values being their dialogues
    '''

    # list of emotion keywords to look for and use as keys
    keywords = ["A", "D", "F", "H", "Sa", "S"]
    # will hold target emotions as key & corresponding dialogues as values
    target_dict = {}

    # keep track of the number of kept rows
    total_rows_detected = 0
    # go over the dataframe once for each keyword
    for keyword in keywords:
        target_dict[keyword] = []
        to_remove = []      # record the row numbers that have the target emotion keyword
        for i in range(0, org_dataframe.shape[0]):
            if keyword in (org_dataframe.loc[i, "PE"] + ":" + org_dataframe.loc[i, "Mood"]).split(":"):     # create a searchabe list of emotion keywords
                target_dict[keyword].append(org_dataframe.loc[i, "Sentence"])                               # append the sentence to a list of sentences for the keyword
                to_remove.append(i)                                                                         # record the row number of the sentence
                total_rows_detected += 1
        org_dataframe.drop(to_remove, axis = 0, inplace = True)                                             # remove the detected rows since they will no longer be needed
        org_dataframe.reset_index(drop = True, inplace = True)                                              # reset the index to prevent subscription problems down the road
        to_remove = []

    print("A total of {} rows were detected & saved.\n".format(total_rows_detected))

    for keyword in target_dict.keys():
        print("{} sentences in {}".format(len(target_dict[keyword]), keyword))

    print("\nAttempting to merge Sa & S into one entry...", end = "")
    for sentence in target_dict["S"]:
        target_dict["Sa"].append(sentence)
    print(" Complete.")
    del target_dict["S"]

    print("After merging Sa & S:\n")
    for keyword in target_dict.keys():
        print("{} sentences in {}".format(len(target_dict[keyword]), keyword))
    return target_dict


def export_dict_txt(org_dict):
    if (not(os.path.exists("./cleaned-data"))):
        os.makedirs("./cleaned-data")

    with open("./cleaned-data/alm_sents.txt", "w") as f:
        f.write(json.dumps(org_dict))

if (__name__) == "__main__":
    aio_dataframe = rm_useless_columns(all_into_one())
    aio_dataframe = rm_nn_rows(aio_dataframe)           # dataframe currently is empty of rows where all emotions are NN:NN
    target_dict = keep_target_emotions(aio_dataframe)
    export_dict_txt(target_dict)
    
    