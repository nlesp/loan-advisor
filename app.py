
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
import matplotlib.pyplot as plt
import plotly.express as px

# 2. Create the app object /  Initialize an instance of FastAPI
#chart = functools.partial(st.plotly_chart, use_container_width=True)

data_train = pd.read_csv('application_train.csv')
headers = {'Content-Type': 'application/json'}
#url_id = "http://127.0.0.1:8000/predict"
#url_list = "http://127.0.0.1:8000/list"
url_id = "https://loan-advisor-api.herokuapp.com/predict"
url_list = "https://loan-advisor-api.herokuapp.com/list"

"""API - load list of clients""" 
id_list_response = requests.get(url_list, headers=headers)
id_list = json.loads(id_list_response.content)  #parse bytes data with json module

def main():
    st.title("Bank Helper")
    

    #payload = st.selectbox('Choose Id client', id_list, help = 'Filter report to show only one id client')
    #id_client = st.selectbox('Choose Id client', data_train['SK_ID_CURR'].tolist(), help = 'Filter report to show only one id client')
    id_client = st.selectbox('Choose Id client', id_list, help = 'Filter report to show only one id client')
    payload = {"id": id_client}
    pred = requests.post(url_id, headers=headers, json=payload)
    result = float(pred.content)
    if st.button("Predict"):
        st.success('Your solvency is at {:.0%}'.format(round(result, 4)))
        #st.success("The score is "+str(round(prediction, 4))+" for the client "+str(id))
        id_score = [1-result,result]
        names=['0', '1']
        #fig, ax = plt.subplots()
        fig = px.pie(values = id_score,names=names)
        fig.show()
        st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
        #plt.show()
        
if __name__=='__main__':
    main()
