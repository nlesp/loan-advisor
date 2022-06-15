
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:39:04 2020
@author:
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("pipeline_bank.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/predict_proba',methods=["Get"])
def predict_note():
    
    """Let's finde the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: id
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    id = request.args.get("id")

    col_index = len(data_train.columns)
    row_index =np.where(data_train['SK_ID_CURR'] == id)
    column_value_id = data_train.iloc[row_index[0][0], 1:col_index]
    df_column_value_id = column_value_id.to_frame().T

    prediction=classifier.predict_proba(df_column_value_id)[:,1]
    print(prediction)
    return "The score is "+str(round(prediction, 4))+" for the client "+str(id)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    