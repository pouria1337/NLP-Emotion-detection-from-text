# NLP-Emotion-detection-from-text
## Overview
This repository contains the implementation of an automatic model to extract emotions from English texts from 5470 memories using Deep Learning. This project was developed as part of my Master's thesis.

## Approach
The model employs a combination of a deep learning language model and Information Retrieval methods. It was trained and tested on 5477 labeled memories out of the 7666 available in the ISEAR dataset, aiming to detect five distinct emotions.

## Metrics
The performance metrics achieved by the model are detailed below. Please note that these metrics may differ from the actual code since TF-IDF filtering was omitted from the code but was included in the thesis analysis.

### Table 1: Overall Accuracy
|           | Random Forest | SVM   | G-Boosted Tree | Logistic_regression|
|-----------|---------------|-------|----------------|--------------------|
| Accuracy  | 0.695         | 0.721 | 0.695          | 0.673              |
| F1-score  | 0.694         | 0.719 | 0.693          | 0.669              |
| Precision | 0.696         | 0.723 | 0.695          | 0.671              |
| Recall    | 0.695         | 0.721 | 0.695          | 0.673              |

### Table 2: Accuracy per Emotion
|     Emotion    |     Evaluation metrics                  |     Ranking                   | SVM                           | RF                            | GBT                           |
|----------------|-----------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|     Anger      |     F-score     <br>Precision     <br>Recall    |     0.56     <br>0.59     <br>0.53    |     0.63     <br>0.60     <br>0.67    |     0.60     <br>0.59     <br>0.62    |     0.60     <br>0.60     <br>0.61    |
|     Disgust    |     F-score     <br>Precision     <br>Recall    |     0.56     <br>0.67     <br>0.49    |     0.60     <br>0.65     <br>0.55    |     0.58     <br>0.59     <br>0.57    |     0.58     <br>0.61     <br>0.55    |
|     Fear       |     F-score     <br>Precision     <br>Recall    |     0.59     <br>0.79     <br>0.48    |     0.75     <br>0.75     <br>0.74    |     0.73     <br>0.73     <br>0.73    |     0.73     <br>0.72     <br>0.73    |
|     Joy        |     F-score     <br>Precision     <br>Recall    |     0.87     <br>0.86     <br>0.88    |     0.88     <br>0.86     <br>0.91    |     0.87     <br>0.85     <br>0.89    |     0.87     <br>0.85     <br>0.90    |
|     Sadness    |     F-score     <br>Precision     <br>Recall    |     0.63     <br>0.50     <br>0.87    |     0.73     <br>0.74     <br>0.72    |     0.70     <br>0.72     <br>0.69    |     0.72     <br>0.71     <br>0.72    |

## Datasets Used

### ISEAR Dataset
Originally in .mdb format, this dataset was converted to .xlsx for better accessibility. Using Python and the Pandas library, the data was preprocessed to remove unwanted columns and insignificant rows. [Link](https://www.unige.ch/cisa/research/materials-and-online-research/research-material/)

### NRC Lexicon
This .txt formatted dataset provides a binary classification for words and their relation to emotions. It was processed to connect words with corresponding emotions and to create respective dataframes. [Link](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

### Affect Data
Also in .txt format, this dataset required reshaping to align the data and corresponding emotions into manageable dataframes. Preprocessing involved the removal of dialogues too vague for representing emotions. [Link](http://people.rc.rit.edu/~coagla/affectdata/index.html)
