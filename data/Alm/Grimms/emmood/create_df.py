import pandas as pd

df_grimms = pd.read_csv("output_file.txt", sep='\t', names=['SentID:SentID', 'PrimaryEmotion', 'Mood', 'Sentence'])
print(df_grimms)