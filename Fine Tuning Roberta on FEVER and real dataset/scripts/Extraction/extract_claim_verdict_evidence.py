
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import  re

# extract claim

data = pd.read_csv(r'final_data_df.csv')
df_factly = data[data['sitename']=='FACTLY'].copy()
df_factly.reset_index(inplace = True)
# webscraping to specifically get claim again.

link = 'https://factly.in/no-swedish-newspaper-has-published-the-story-narrated-in-the-post/'
html_link = requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})


soup.find_all('blockquote',class_ = "wp-block-quote")
i = soup.find_all('blockquote',class_ = "wp-block-quote")[0]
soup.find_all(class_ = "wp-block-quote")[0].get_text(separator = '.', strip=True).split('.')



for item in i.find_all('p'):
	print(item.text)

def get_claim_evidence_label(link):
	try :
		html_of_link = requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(html_of_link.text, "html.parser")
		#blocks = soup.find_all('blockquote',class_ = "wp-block-quote")
		blocks = soup.find_all('blockquote')
		if len(blocks) == 1:
			block = blocks[0]
			items = block.find_all('p')
			if len(items)> 1 :
				claim = items[0].get_text()[7:]
				evidence =  items[1].get_text()[6:]
				label = items[1].find_all('strong')[-1].get_text()
			else :
				s = items[0].get_text().split('Fact:')
				claim = s[0][7:]
				evidence = s[1]
				label = items[0].find_all('strong')[-1].get_text()
			return pd.Series([claim,evidence,label])
		elif len(blocks) > 1:
			claim = []
			evidence = []
			label = []
			for block in blocks:
				if re.match('Claim:',block.get_text()):
					items = block.find_all('p')
					c = items[0].get_text()[7:]
					e = items[1].get_text()[6:]
					l = items[1].find_all('strong')[1].get_text()
					claim.append(c)
					evidence.append(e)
					label.append(l)
			return pd.Series([claim,evidence,label])
		else :
			return pd.Series(['', '', ''])

	except :
		return pd.Series(['','',''])


get_claim_evidence_label(link)


""" Appending to data frame"""
df_factly[['claim','evidence','label']] = ''

for index,row in df_factly.iterrows():
	print(row['pageurl'])
	s = get_claim_evidence_label(row['pageurl'])
	print(s)
	df_factly.loc[index, 'claim'] = s[0]
	df_factly.loc[index, 'evidence'] = s[1]
	df_factly.loc[index, 'label'] = s[2]
	time.sleep(1)
	print(index,' is done')



df_factly.to_csv('factly_claim_evi_data_ver2.csv')
df_not_scrapped = df_factly[df_factly['claim']=='']
k = get_claim_evidence_label(df_not_scrapped.loc[23,'pageurl'])
link = df_not_scrapped.loc[23,'pageurl']
get_claim_evidence_label(link)

# # extract evidence from articles where we didn't get
index = df_not_scrapped.index
for i in index:
	ss = get_claim_evidence_label(df_factly.loc[i,'pageurl'])
	#print(s)
	df_factly.loc[i, 'claim'] = str(ss[0])
	df_factly.loc[i, 'evidence'] = str(ss[1])
	df_factly.loc[i, 'label'] = str(ss[2])
	time.sleep(1)
	print(i,' is done')




# Modelling part

""" converting data into feverous format """

import jsonlines


with jsonlines.open(r"C:\Users\prudh\Downloads\feverous_train_challenges.jsonl",'r') as reader:
	lst = [obj for obj in reader]


df_stats = df_factly.copy(deep =True)
df_stats['claim_tokens'] = df_stats.claim.str.split()
df_stats['claims_len']= df_stats['claim_tokens'].apply(lambda x : len(x))
df_stats[df_stats['claims_len']!=0]['claims_len'].mean()
