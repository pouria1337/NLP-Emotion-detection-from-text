# dataset: http://people.rc.rit.edu/~coagla/affectdata/index.html
# each author has multiple labeled stories each in a separate file
# merge all stories from all authors into one file
# output three txt files 

# import
import pandas as pd
import os

# global variables
grimm_files = "data/Alm/Grimms/emmood"          # forward slash for better compatibility
andersen_files = "data/Alm/HCAndersen/emmood"       
potter_files = "data/Alm/Potter/emmood"

# function definitions
def get_txt_list(files_dir):
    '''given a directory full of files, return a list of .txt file names'''
    txt_files = []
    for filename in os.listdir(files_dir):
        if filename.endswith(".txt"):
            txt_files.append(files_dir + "/" + filename)
    return txt_files

def merge_and_save(file_list, filename):
    '''to recieve a list of file names & return a songle dataframe containing their merged output'''
    if (not(os.path.exists("./merged-data"))):
        os.makedirs("./merged-data")
    
    # full path of the output file
    output = "./merged-data/" + filename
    with open(output, 'w') as outfile:
        for textfile in file_list:
            with open(textfile, 'r') as infile:
                outfile.write(infile.read())

# main()
if __name__ == "__main__":
    merge_and_save(get_txt_list(grimm_files), "grimm_merged.txt")
    merge_and_save(get_txt_list(andersen_files), "andersen_merged.txt")
    merge_and_save(get_txt_list(potter_files), "potter_merged.txt")