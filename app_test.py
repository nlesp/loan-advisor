
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:39:04 2020
@author:
"""
# 1. Library imports
import requests
import json

#import sklearn
#from lightgbm import LGBMClassifier
# 2. Create the app object /  Initialize an instance of FastAPI
#url = 'http://127.0.0.1:8000/predict'
url = 'https://loan-advisor-api.herokuapp.com/predict'
def main():
    m = 100004
    payload = {"id": m}

    #payload = json.dumps({ "id": 100005}) if data
    

    headers = {'Content-Type': 'application/json'}
    #response = requests.post(url, headers=headers, json=payload)

    pred = requests.post(url, headers=headers, json=payload)
    result = float(pred.content)

    #score = float(response.content)
    #score2 = 1 - score
    print(result)
    #print('The score of the client is :'+str(1-response.content))
    print('The score of the client is {}'.format(type(payload)))

#uvicorn app:app --reload

if __name__=='__main__':
    main()