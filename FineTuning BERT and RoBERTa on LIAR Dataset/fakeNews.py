import numpy as np
import streamlit as st
from transformers import AutoModel, BertTokenizerFast
from transformers import RobertaTokenizerFast
import torch
import torch.nn as nn


class BERT_Arch(nn.Module):
    def __init__(self, bert):  
      super(BERT_Arch, self).__init__()
      self.bert = bert   
      self.dropout = nn.Dropout(0.1)            # dropout layer
      self.relu =  nn.ReLU()                    # relu activation function
      self.fc1 = nn.Linear(768,512)             # dense layer 1
      self.fc2 = nn.Linear(512,6)               # dense layer 2 (Output layer)
      self.softmax = nn.LogSoftmax(dim=1)       # softmax activation function
    def forward(self, sent_id, mask):           # define the forward pass  
      cls_hs = self.bert(sent_id, attention_mask=mask)['pooler_output']
                                                # pass the inputs to the model
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      x = self.fc2(x)                           # output layer
      x = self.softmax(x)                       # apply softmax activation
      return x

#tokenizer is not hashable

class StreamlitApp:

    def __init__(self,path="./changed_weights_bert.pt"):
        pass


    def construct_app(self):

        st.write("Choose the model you want to use:")
        st.write("1: Fixed BERT Model with Fine Tuning")
        st.write("2: Fixed RoBERTa Model with Fine Tuning")
        st.write("3: Changed Weight of BERT Model with Fine Tuning")
        st.write("4: Changed Weight of RoBERTa Model with Fine Tuning")

        st.write("\n")
        choice=st.text_input("Enter the Choice of Model (1/2/3/4)")

        if choice!="":
            choice=int(choice)
            if choice==1 or choice==3:
                self.base = AutoModel.from_pretrained('bert-base-uncased')
                self.tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
                self.model = BERT_Arch(self.base)
            else:
                self.base = AutoModel.from_pretrained("roberta-base")
                self.tokenizer = RobertaTokenizerFast.from_pretrained("roberta-base")
                self.model = BERT_Arch(self.base)
        
        models={1:"./fixed_weights_bert.pt",2:"./fixed_weights_roberta.pt",3:"./changed_weights_bert.pt",4:"./changed_weights_roberta.pt"}



        path=""
        if choice in models:
            path=models[choice]
        else:
            path="./changed_weights_bert.pt"

        

        text = st.text_input("Enter Some Text")

        if text!="":

            text=[text]
            self.model.load_state_dict(torch.load(path))
            # tokenize and encode sequences in the test set
            MAX_LENGHT = 100
            tokens_unseen = self.tokenizer.batch_encode_plus(text,max_length = MAX_LENGHT,pad_to_max_length=True,truncation=True)

            label={0:"False",1:"Half-True",2:"Mostly true",3:"True",4:"Barely True",5:"Pants-fire"}

            unseen_seq = torch.tensor(tokens_unseen['input_ids'])
            unseen_mask = torch.tensor(tokens_unseen['attention_mask'])

            with torch.no_grad():
                preds = self.model(unseen_seq, unseen_mask)
                preds = preds.detach().cpu().numpy()

            preds = np.argmax(preds, axis = 1)
            preds=label[int(preds)]

            st.write("This news is ",preds)


sa = StreamlitApp()
sa.construct_app()