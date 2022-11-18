# Fake-News-Detection

The work is divided into 3 sections:

## Fine Tuning on LIAR Dataset : 

To run the code for inference, we need to first install the dependecies by  `pip install requirements.txt`. After that we need to download the models from `https://drive.google.com/drive/folders/1Ev2jcCSymR_jMCTXTHJU0AR46IiGBkYK?usp=sharing`. Then we need to use the command `streamlit run fakeNews.py ` to open the interface. Where we can choose which model to use and get inference corresponding to that. The model will be downloaded at first, so while first inference it will take some time. 

Jupyter notebook has the whole code. These can be run in kaggle once uploaded, they don't need any datasets as the dataset are being downloaded from the huggingface website. 


## Fine Tuning on FEVEROUS Dataset
    
To run the code for data collection, we need to run each ipynb in scripts/webscraping.

To run the code for claim,evidence, lable extraction, run the code - `python -m scripts/extract_claim_verdict_evidence/extract_claim_verdict_evidence.py` 

To run the code for model fine tuning, run the code `python -m scripts/train_verdict_predictor.py`

To run the code for score evaluation, run the code   `python -m scripts/evaluate_verdict_predictor.py`

For feverous data, use the link - https://fever.ai/dataset/feverous.html 
    
    
## CompareNet++
Host the dataset in some drive and provide link. And then steps to run the model. </br>
https://github.com/BUPT-GAMMA/CompareNet_FakeNewsDetection/releases/tag/dataset
https://drive.google.com/file/d/1njY42YQD5Mzsx2MKkI_DdtCk5OUKgaqq/view

Test Data should be as per below hierarchy.

```
───data
    ├── fakeNews
    │   ├── adjs
    │   │   ├── train
    │   │   ├── dev
    │   │   └── test
    │   ├── fulltrain.csv
    │   ├── balancedtest.csv
    │   ├── test.xlsx
    │   ├── entityDescCorpus.pkl
    │   └── entity_feature_transE.pkl
    └── stopwords_en.txt

```


















