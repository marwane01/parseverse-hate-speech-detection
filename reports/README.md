# Hate Speech Detection | Classification
## Description
Dataset for the paper Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM.

## Entries
entries: 25296 

## URL
https://github.com/t-davidson/hate-speech-and-offensive-language/tree/master

## File Format
csv

| Column | Description       |
| ----- | ------------------ |
|tweet| a classification label, [23 classes](./data/classes.txt) |
|count | number of CrowdFlower users who coded each tweet (min is 3, sometimes more users coded a tweet when judgments were determined to be unreliable by CF).
|hate_speech | number of CF users who judged the tweet to be hate speech.
|offensive_language | number of CF users who judged the tweet to be offensive.
|neither | number of CF users who judged the tweet to be neither offensive nor non-offensive.
|class | class label for majority of CF users. 0 - hate speech 1 - offensive language 2 - neither

