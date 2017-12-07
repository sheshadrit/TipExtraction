# TipExtraction
Prerequisite libraries required: pattern and spcay

Installing library patter for python 3.0+:
1. Download pattern-master.zip from https://github.com/clips/pattern
2. Extract pattern-master.zip
3. Copy folder pattern to %PATH%\Anaconda3\Lib\site-packages

Installing library spacy for python 3.0+:
Follow this link https://spacy.io/usage/

Files List:
TipExtractor.py : Uses spacy and pattern library to give summary of tip highlighted by uses most frequently
TipExtractionWithoutSpacy.py : Gives you a csv file contatining two columns review and extarcted tip
ReviewsAndTips.csv: A csv file contatining two columns review and extarcted tip
TipsAndTheirRank.csv: Contains list of sentences from the extracted tip from ReviewsAndTips.csv file and there corresponding ranking i.e. how frequently they have used by the reviewers
FinalExtractedTips.txt: Contains list of sentences from the extracted tip from ReviewsAndTips.csv file which are most frequently used by reviewers


