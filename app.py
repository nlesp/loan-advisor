from unittest import result
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from processing_functions import add_variable


data_train = pd.read_csv('application_train.csv')
pickle_in = open("pipeline_bank.pkl","rb")
classifier=pickle.load(pickle_in)

add_variable(data_train)

#@app.route('/predict',methods=["Get"])
def predict_note(id):
    
    """Let's Authenticate the Banks Note 
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

    col_index = len(data_train.columns)
    row_index =np.where(data_train['SK_ID_CURR'] == id)
    column_value_id = data_train.iloc[row_index[0][0], 1:col_index]
    df_column_value_id = column_value_id.to_frame().T
    prediction=classifier.predict_proba(df_column_value_id)[:,1]
    print(prediction)
    return prediction

def main():
    st.title("Bank Helper")

    
    id = st.selectbox('Choose Id client', data_train, help = 'Filter report to show only one id client')
    
    if st.button("Predict"):
        result=predict_note(id)
        st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()