import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/predict',methods=["Get"])
def predict_bank(type_client,flag,region_rating,region_rating_city,amount):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: type_client
        in: query
        type: string
        required: true
      - name: flag
        in: query
        type: string
        required: true
      - name: region_rating
        in: query
        type: number
        required: true
      - name: region_rating_city
        in: query
        type: number
        required: true
      - name: amount
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[type_client,flag,region_rating,region_rating_city,amount]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Helper")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Helper ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    type_client = st.text_input("Type of client","Type Here")
    flag = st.text_input("flag own reality","Type Here")
    region_rating = st.text_input("Region Rating","Type Here")
    region_rating_city = st.text_input("Region Rating City","Type Here")
    amount = st.text_input("Amount of credit","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_bank(type_client,flag,region_rating,region_rating_city,amount)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()