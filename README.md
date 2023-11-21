# NLP-Emotion-detection-from-text
## Automatic model to extract emotions from English texts via Deep Learning
This was my Master's thesis and also my final project for completing the Harvard CS50 course. 

In this approach, I used a deep learning language model in combination with Information Retrieval methods to detect emotions from 5477 labeled memories of the 7666 in the ISEAR dataset. Below, I have provided the metrics I was able to achieve in detecting five emotions.

The following matrics may differ from the actual code since I omitted TF-IDF filtering from the code. I did, however, do TF-IDF filtering for my thesis.

|           | Random Forest | SVM   | G-Boosted Tree |
|-----------|---------------|-------|----------------|
| Accuracy  | 0.7           | 0.721 | 0.703          |
| F1-score  | 0.698         | 0.718 | 0.7            |
| Precision | 0.702         | 0.723 | 0.702          |
| Recall    | 0.699         | 0.720 | 0.702          |


|     Emotion    |     Evaluation metrics                  |     Ranking                   | SVM                           | RF                            | GBT                           |
|----------------|-----------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|     Anger      |     F-score     <br>Precision     <br>Recall    |     0.56     <br>0.59     <br>0.53    |     0.63     <br>0.60     <br>0.67    |     0.60     <br>0.59     <br>0.62    |     0.60     <br>0.60     <br>0.61    |
|     Disgust    |     F-score     <br>Precision     <br>Recall    |     0.56     <br>0.67     <br>0.49    |     0.60     <br>0.65     <br>0.55    |     0.58     <br>0.59     <br>0.57    |     0.58     <br>0.61     <br>0.55    |
|     Fear       |     F-score     <br>Precision     <br>Recall    |     0.59     <br>0.79     <br>0.48    |     0.75     <br>0.75     <br>0.74    |     0.73     <br>0.73     <br>0.73    |     0.73     <br>0.72     <br>0.73    |
|     Joy        |     F-score     <br>Precision     <br>Recall    |     0.87     <br>0.86     <br>0.88    |     0.88     <br>0.86     <br>0.91    |     0.87     <br>0.85     <br>0.89    |     0.87     <br>0.85     <br>0.90    |
|     Sadness    |     F-score     <br>Precision     <br>Recall    |     0.63     <br>0.50     <br>0.87    |     0.73     <br>0.74     <br>0.72    |     0.70     <br>0.72     <br>0.69    |     0.72     <br>0.71     <br>0.72    |

## I used the following datasets 
* ISEAR Dataset [Link](https://www.unige.ch/cisa/research/materials-and-online-research/research-material/)

  This dataset was in .mdb format which had to be opened by Microsoft Access. I converted it to .csv format and used Python and the Pandas library to preprocess them, remove unwanted columns, and remove rows with no significance.
* NRC Lexicon [Link](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

  This dataset was in .txt format with a binary classification for words and their relation to emotions. As the above dataset, I utilized Python and the Pandas library to connect words with corresponding emotions and created respective dataframes.
* Affect Data [Link](http://people.rc.rit.edu/~coagla/affectdata/index.html)

  This dataset was also in .txt format in an arbitrary written style. Again, with the power of Python and Pandas I reshaped the data and corresponding emotions into managable dataframes. As for pre-processesing, I removed dialogues that were too vague for representing emotions. 
