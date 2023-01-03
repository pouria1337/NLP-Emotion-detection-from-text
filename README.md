# NLP-Emotion-detection-from-text
## Automatic model to extract emotions from English texts via Deep Learning
This was my Master's thesis. 

In this approach, I used a deep learning language model in combination with Information Retrieval methods to detect emotions from 5428 labeled memories of the 7666 in the ISEAR dataset. Below, I have provided the metrics I was able to achieve in detecting five emotions.


|           | Random Forest | SVM   | G-Boosted Tree |
|-----------|---------------|-------|----------------|
| Accuracy  | 0.7           | 0.723 | 0.703          |
| F1-score  | 0.698         | 0.718 | 0.7            |
| Precision | 0.702         | 0.723 | 0.702          |
| Recall    | 0.699         | 0.720 | 0.702          |


|     Emotion    |     Evaluation metrics                  |     Ranking                   | SVM                           | RF                            | GBT                           |
|----------------|-----------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|     Anger      |     F-score     Precision     Recall    |     0.56     0.59     0.53    |     0.63     0.60     0.67    |     0.60     0.59     0.62    |     0.60     0.60     0.61    |
|     Disgust    |     F-score     Precision     Recall    |     0.56     0.67     0.49    |     0.60     0.65     0.55    |     0.58     0.59     0.57    |     0.58     0.61     0.55    |
|     Fear       |     F-score     Precision     Recall    |     0.59     0.79     0.48    |     0.75     0.75     0.74    |     0.73     0.73     0.73    |     0.73     0.72     0.73    |
|     Joy        |     F-score     Precision     Recall    |     0.87     0.86     0.88    |     0.88     0.86     0.91    |     0.87     0.85     0.89    |     0.87     0.85     0.90    |
|     Sadness    |     F-score     Precision     Recall    |     0.63     0.50     0.87    |     0.73     0.74     0.72    |     0.70     0.72     0.69    |     0.72     0.71     0.72    |
