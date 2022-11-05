# NLP-Emotion-detection-from-text
## Automatic model to extract emotions from English texts via Deep Learning
In this approach, I use a deep learning language model which is pre-trained and fine-tuned for semantic searches to detect emotions from 5428 labeled memories from the ISEAR dataset. To achieve this goal, I first model each target emotion with a series of carefully selected words from two datasets: NRC Lexicon and Affect Data. Then, I will calcualte the similarity of each memory with that of each modeled emotion. Each memory will have five numbers associated with each of the targeted emotions; these will be the features upon which I will train various ML classifiers. The process is as follows:

i. Clean ISEAR dataset, NRC Lexicon according to target emotions
ii. Deploy TF-IDF weighing on Affect Data
iii. Extract top TF-IDF words from NRC Lexicon and model each emotion accordingly
iiii. Load off-the-shelf fine-tuned language model & calculate semantic similarity of each memory and modeled emotions
iiiii. Feed created similarities to ML classifiers, train, test and report accuracy metrics


Random_Forest	SVM	G-Boosted_Tree
Accuracy	0.700	0.721	0.703
F1-score	0.698	0.718	0.700
Precision	0.702	0.723	0.702
Recall	0.699	0.720	0.702
