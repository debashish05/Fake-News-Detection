# Fake-News-Detection

The work is divided into 3 sections:

## Fine Tuning on LIAR Dataset : 

To run the code for inference, we need to first install the dependecies by  `pip install requirements.txt`. After that we need to download the models from `https://drive.google.com/drive/folders/1Ev2jcCSymR_jMCTXTHJU0AR46IiGBkYK?usp=sharing`. Then we need to use the command `streamlit run fakeNews.py ` to open the interface. Where we can choose which model to use and get inference corresponding to that. The model will be downloaded at first, so while first inference it will take some time. 

Jupyter notebook has the whole code. These can be run in kaggle once uploaded, they don't need any datasets as the dataset are being downloaded from the huggingface website. 


## Fine Tuning on FEVEROUS Dataset
    Host the dataset in some drive and provide link. And then steps to run the model.

## CompareNet++
    Host the dataset in some drive and provide link. And then steps to run the model.


















 ### Evaluating performance of models trained on FEVER data on REAL claims data

 
 
 #### Data Extraction :
  
 All the code is inside /scripts. Scrpits/webscrapping has the notebooks to run and download raw data from each website - FActly, altnews, opindia, boomlive. 
 
#### Claim Evidence and Verdict Extraction

scripts/extract_claim_verdict_evidence.py can be run to extract claim, evidence from content. Input is the data with content and output is saved as csv file. 

#### Training and Evaluation

scripts/train_verdict_predictor, scripts/evaluate_verdict_predictor is used from baseline for FEVEROUS data. It is modified to used for our format. 



#### data 

All the data collected, cleaned data with claim, evidence, verdict is in data folder. 
