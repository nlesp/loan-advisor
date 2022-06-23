
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:39:04 2020
@author:
"""
# 1. Library imports
import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from processing_functions import add_variable, get_client
from pydantic import BaseModel

#import sklearn
#from lightgbm import LGBMClassifier
# 2. Create the app object /  Initialize an instance of FastAPI
app = FastAPI()


pickle_in = open("pipeline_bank.pkl","rb")
pipeline_process=pickle.load(pickle_in)

data_train = pd.read_csv('application_train.csv')

add_variable(data_train)

#get_client(id,data_train)
@app.get('/')
def index():
    col_index = len(data_train.columns)
    return {'Welcome to this API for loan advisor'}

#@app.get('/{name}')
#def get_name(name : str):
#    return {'Welcome ': f'{name}'}
@app.get('/list')
def get_list_id():
    return data_train['SK_ID_CURR'].tolist()
#Class which describes a single id
class Item(BaseModel):
    id: float

@app.post('/predict')
def predict_bank(item : Item):
    data = item.dict()
    #col_index = len(data_train.columns)
    row_index = data_train['SK_ID_CURR'].tolist().index(data['id'])
    column_value_id = data_train.iloc[row_index][2:]
    #row_index =np.where(data_train['SK_ID_CURR'] == data['id'])
    #column_value_id = data_train.iloc[row_index[0][0], 1:col_index]
    df_column_value_id = column_value_id.to_frame().T
    prediction=pipeline_process.predict_proba(df_column_value_id)[:,1]
    id_score = str(prediction[0])
    print(id_score)
    return id_score 

#@app.get('/predict/{id}')
#def predict_note(id):

    col_index = len(data_train.columns)
    #row_index =np.where(data_train['SK_ID_CURR'] == id)
    #column_value_id = data_train.iloc[row_index[0][0], 1:col_index]
    #df_column_value_id = column_value_id.to_frame().T
    #prediction=pipeline_process.predict_proba(df_column_value_id)[:,1]
    #print(prediction)
    #return prediction
"""
@app.get('/')
def get_name():
    col_index = len(data_train.columns)
    return {'Welcome': len(data_train.columns)}


# 2. Define the default route 
@app.get("/")
def root():
    return {"message": "Welcome to Your Sentiment Classification FastAPI"}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict/')
def predict_note(id):

    col_index = len(data_train.columns)
    row_index =np.where(data_train['SK_ID_CURR'] == id)
    column_value_id = data_train.iloc[row_index[0][0], 1:col_index]
    df_column_value_id = column_value_id.to_frame().T
    prediction=pipeline_process.predict_proba(df_column_value_id)[:,1]
    print(prediction)
    return prediction

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000

"""

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload