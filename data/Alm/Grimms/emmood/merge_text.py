import os
import pandas as pd
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

x = getListOfFiles("./")

filenames = x
#print(filenames)

#with open("output_file.txt", "w") as outfile:
#    for filename in filenames:
#       with open(filename) as infile:
#            contents = infile.read()
#            outfile.write(contents)
grimm_df = pd.read_csv('106_the_poor_millers_boy_and_the_cat.txt', sep='\t',
                        names=['SentID:SentID', 'PrimaryEmotion', 'Mood', 'Sentence'])

print(grimm_df.head(15))