# gives TF-IDF weight to words in the cleaned Alm dataset
# outputs a .csv with one column being the word, the other being the tf-idf score

# import
import json
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer

# global variables
cleaned_data_path = "./cleaned-data/alm_sents.txt"
stop_words = [
    "a", "an", "the", "and", "or", "but", "not", "for", "in", "to", "on", "of",
    "at", "by", "from", "with", "up", "down", "in", "out", "over", "under",
    "again", "further", "here", "there", "now", "then", "also", "because", "as",
    "so", "if", "else", "while", "than", "too", "very", "just", "can", "could",
    "may", "might", "must", "should", "will", "would", "shall", "do", "does",
    "did", "doing", "done", "has", "have", "had", "been", "being", "be",
    "is", "am", "are", "was", "were", "been", "go", "goes", "went", "gone",
    "come", "comes", "came", "come", "get", "gets", "got", "gotten", "say",
    "says", "said", "said", "see", "sees", "saw", "seen", "tell", "tells", "told",
    "told", "know", "knows", "knew", "known", "ask", "asks", "asked", "asked",
    "think", "thinks", "thought", "thought", "feel", "feels", "felt", "felt",
    "try", "tries", "tried", "tried", "find", "finds", "found", "found",
    "give", "gives", "gave", "given", "make", "makes", "made", "made",
    "take", "takes", "took", "taken", "he", "He", "him", "his", "His", "she", 
    "She", "her", "hers", "They", "they", "them", "you", "You", "It", "it", "That", 
    "that", "my", "me", "we", "us", "thier", "theirs", "your", "yours", "all", "one", 
    "what", "when", "where", "why", "who", "which", "this", "This", "mr", "Mr", "Mr."
]

# function definitions
def import_data():
    '''
    open the saved dictionary text file of affect data sentences with target emotions
    and return it
    '''
    with open(cleaned_data_path, "r") as f:
        json_string = f.read()

    my_dict = json.loads(json_string)
    return my_dict


def give_weight(org_dict, emotion_keyword):
    '''
    given a dictionary of keys & values, it creates a tf-idf score for each value
    of a given emotion_keyword & return a dataframe with columns as words and rows as 
    individual scores. 
    To get the tf-idf of a word, the values of each column must be summed up.
    '''
    anger_corpus = org_dict[emotion_keyword]
    vectorizer = TfidfVectorizer(stop_words = stop_words)
    X = vectorizer.fit_transform(anger_corpus)
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    # attemp to remove numerical columns from dataframe
    # get a list of column names
    column_names = list(df.columns.values)
    # record invalid column names
    invalid_columns = []
    for name in column_names:
        if not(name.isalpha()):
            invalid_columns.append(name)
    # remove invalid column names
    df.drop(invalid_columns, axis = 1, inplace = True)
    return df


def f(org_dict):
    '''
    sum, sort and save tf-idf scores for all emotion keywords
    save each dataframe to a separate .csv file
    '''
    if (not(os.path.exists("./tf-idf-files"))):
        os.makedirs("./tf-idf-files")

    
    emotion_keys = ["A", "D", "F", "H", "Sa"]       # list of emotion keywords
    for keyword in emotion_keys:
        temp_df = give_weight(org_dict, keyword)                              # this returns a tf-idf dataframe for a specific emtoin which needs to be summed & sorted
        list_of_scores = []                                                   # holds a list of scores for each word of an emotion
        for column in temp_df.columns:                                        # go over each column (word) in the tf-idf dataframe
            list_of_scores.append(sum(list(temp_df[column])))                 # sum all the values for a column, which is a word
        unsorted_df = pd.DataFrame(data = list_of_scores, 
                                   index = temp_df.columns, 
                                   columns = ["TF-IDF"])                      # create a dataframe where one column is words, the other its corresponding scores
        sorted_df = unsorted_df.sort_values(by = ["TF-IDF"], 
                                            ascending = False)
        sorted_df.to_csv("./tf-idf-files/" + keyword + "-tf-idf.csv")
        print(sorted_df)

if (__name__) == "__main__":
    keyed_sentences = import_data()
    f(keyed_sentences)