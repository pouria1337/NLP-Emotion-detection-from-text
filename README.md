# NLP-Emotion-detection-from-text
## Overview
This repository contains the implementation of an automatic model to extract emotions from English texts from 5470 memories using Deep Learning. This project was developed as part of my Master's thesis.

## Approach
The model employs a combination of a deep learning language model and Information Retrieval methods. It was trained and tested on 5470 labeled memories out of the 7666 available in the ISEAR dataset, aiming to detect five distinct emotions.

## Metrics
The performance metrics achieved by the model are detailed below. Please note that these metrics may differ from the actual code since TF-IDF filtering was omitted from the code but was included in the thesis analysis.

### Table 1: Overall Accuracy
|           | Random forest | SVM   | G-Boosting tree| Logistic regression|
|-----------|---------------|-------|----------------|--------------------|
| Accuracy  | 0.695         | 0.721 | 0.695          | 0.673              |
| F1-score  | 0.694         | 0.719 | 0.693          | 0.669              |
| Precision | 0.696         | 0.723 | 0.695          | 0.671              |
| Recall    | 0.695         | 0.721 | 0.695          | 0.673              |

### Table 2: Accuracy per Emotion
|Emotion|Metrics  |Random forest|SVM |G-Boosting tree|Logistic regression|
|-------|---------|-------------|----|---------------|-------------------|
|anger  |accuracy |0.7          |0.72|0.7            |0.67               |
|       |f1-score |0.61         |0.64|0.6            |0.6                |
|       |precision|0.59         |0.6 |0.59           |0.58               |
|       |recall   |0.63         |0.69|0.61           |0.61               |
|disgust|accuracy |0.7          |0.72|0.7            |0.67               |
|       |f1-score |0.59         |0.61|0.59           |0.55               |
|       |precision|0.61         |0.68|0.62           |0.58               |
|       |recall   |0.57         |0.56|0.56           |0.52               |
|fear   |accuracy |0.7          |0.72|0.7            |0.67               |
|       |f1-score |0.72         |0.73|0.7            |0.65               |
|       |precision|0.72         |0.72|0.69           |0.7                |
|       |recall   |0.71         |0.74|0.71           |0.61               |
|joy    |accuracy |0.7          |0.72|0.7            |0.67               |
|       |f1-score |0.87         |0.89|0.87           |0.85               |
|       |precision|0.86         |0.86|0.86           |0.8                |
|       |recall   |0.89         |0.91|0.89           |0.92               |
|sadness|accuracy |0.7          |0.72|0.7            |0.67               |
|       |f1-score |0.69         |0.73|0.71           |0.7                |
|       |precision|0.7          |0.74|0.71           |0.69               |
|       |recall   |0.68         |0.71|0.71           |0.71               |

## Datasets Used

### ISEAR Dataset
Originally in .mdb format, this dataset was converted to .xlsx for better accessibility. Using Python and the Pandas library, the data was preprocessed to remove unwanted columns and insignificant rows. [Link](https://www.unige.ch/cisa/research/materials-and-online-research/research-material/)

### NRC Lexicon
This .txt formatted dataset provides a binary classification for words and their relation to emotions. It was processed to connect words with corresponding emotions and to create respective dataframes. [Link](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

### Affect Data (Alm)
Also in .txt format, this dataset required reshaping to align the data and corresponding emotions into manageable dataframes. Preprocessing involved the removal of dialogues too vague for representing emotions. [Link](http://people.rc.rit.edu/~coagla/affectdata/index.html)
