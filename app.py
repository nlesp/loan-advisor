
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:39:04 2020
@author:
"""
# 1. Library imports
import requests
import json
import pandas as pd
import streamlit as st

# 2. Create the app object /  Initialize an instance of FastAPI

data_train = pd.read_csv('application_train.csv')
headers = {'Content-Type': 'application/json'}
#url_id = "http://127.0.0.1:8000/predict"
#url_list = "http://127.0.0.1:8000/list"
url_id = "https://loan-advisor-api.herokuapp.com/predict"
url_list = "https://loan-advisor-api.herokuapp.com/list"
def main():
    st.title("Bank Helper")
    
    #id_list = requests.post(url_list, headers=headers, json=payload)
    #payload = st.selectbox('Choose Id client', id_list, help = 'Filter report to show only one id client')
    payload = st.selectbox('Choose Id client', data_train['SK_ID_CURR'].tolist(), help = 'Filter report to show only one id client')
    
    pred = requests.post(url_id, headers=headers, json=payload)
    pred1 = requests.post(url_id, headers=headers, data=payload)
    pred2 = requests.post(url_id, headers=headers, data=json.dumps(payload))
    
    #result = float(pred.content)
    if st.button("Predict"):
        #st.success('The score of the client is {}'.format(pred1.content))
        st.success('The score of the client is {}'.format(pred2.content))
        st.success('The score of the client is {}'.format(pred.content))
        #st.success('The score of the client is {}'.format(float.fromhex(pred.content)))         
        #st.success('The score of the client is {}'.format(result))
        #st.success("The score is "+str(round(prediction, 4))+" for the client "+str(id))
     #   names='0', '1',
      #  id_score = [1-result,result]
     #   fig = plt.pie(id_score,labels=names,labeldistance=1.15)
      #  fig.update_layout(title_text="Client score",title_x=0, yaxis_title=None, xaxis_title=None)

if __name__=='__main__':
    main()
