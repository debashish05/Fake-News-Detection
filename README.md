# Fake-News-Detection

Link to data for CompareNet: https://drive.google.com/drive/folders/1EjhVjxFpSySf_KbKlmpYwJCkcoXayCIm?usp=sharing. 
















 ### Evaluating performance of models trained on FEVER data on REAL claims data

 
 
 #### Data Extraction :
  
 All the code is inside /scripts. Scrpits/webscrapping has the notebooks to run and download raw data from each website - FActly, altnews, opindia, boomlive. 
 
#### Claim Evidence and Verdict Extraction

scripts/extract_claim_verdict_evidence.py can be run to extract claim, evidence from content. Input is the data with content and output is saved as csv file. 

#### Training and Evaluation

scripts/train_verdict_predictor, scripts/evaluate_verdict_predictor is used from baseline for FEVEROUS data. It is modified to used for our format. 
