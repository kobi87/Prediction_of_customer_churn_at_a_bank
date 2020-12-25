import numpy as np
import pickle
import os
import pandas as pd
import streamlit as st 
from PIL import Image

# load transform OneHotEncoder
if os.path.isfile("./OneHotEncoder.pkl"):
  OneHotEncoder = pickle.load(open("./OneHotEncoder.pkl", "rb"))
else:
  raise FileNotFoundError

# load ML model
if os.path.isfile("./model.pkl"):
  classifier = pickle.load(open("./model.pkl", "rb"))
else:
  raise FileNotFoundError

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/transform',methods=["Get"])
def transform(creditscore,geography,gender,age,tenure,balance,numofproducts,hascrcard,isactivemember,estimatedsalary):
    
    echant_ohe_cat = [[geography, gender]]
    echo_numer =  [[creditscore, age,tenure,balance,numofproducts,hascrcard,isactivemember,estimatedsalary]]
    transform = OneHotEncoder.transform(echant_ohe_cat)  
    # Concatenate transform categorical and numeric features 
    sample_out = np.concatenate((echo_numer, transform), axis=1)
    return sample_out

#@app.route('/predict',methods=["Get"])
def predict(sample_in):
 
    prediction=classifier.predict(sample_in)
    print(prediction)
    return prediction

def main():
    #background
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://hicenter.co.il/wp-content/uploads/2016/01/bkg.jpg");
    background-size: cover%;
    background-repeat: no-repeat;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.write("""
    ## ------- **Predict customer churn in a bank using :** ------
    ## ------------- **Voting Ensemble Classifier** ----------------
    As we know, it is much more expensive to sign in a new client than keeping an existing one.
    It is advantageous for banks to know what leads a client towards the decision to leave the company.

    Churn prevention allows companies to develop loyalty programs and retention campaigns to keep as many customers as possible.

    """)
    st.write("""
    This App predicts the likelihood that a **bank customer** will unsubscribe or not.
    """)
    """
    @author: Bilal Khomri
    """
    
    html_temp = """
    <div style="background-color:#ff9966;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction Form</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # App
    geography = st.radio("Country",('France', 'Spain', 'Germany'))
    gender = st.radio("Gender",('Male', 'Female'))
    age = st.slider('Age', 18, 100, 50)
    creditscore = st.slider('Credit Score', 300, 900, 700)
    tenure = st.slider('Tenure Payment Plan', 0, 10, 4)

    balance = st.slider('Balance', 0, 260000, 50000)    
    numofproducts = st.slider('Number of products', 1, 4, 2)
    
    card = st.radio("Has a card ?",('Yes', 'No'))
    if card == 'Yes':
        hascrcard = 1
    else:
        hascrcard = 0
    
    active = st.radio("Is Active Member ?",('Yes', 'No'))
    if active == 'Yes':
        isactivemember = 1
    else:
        isactivemember = 0
        
    estimatedsalary = st.slider('Estimated Salary', 200, 200000, 20000)
    html_temp = """
    <div style="background-color:#ff9966;padding:5px;margin-bottom:20px"> </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    result=""
    if st.button("Predict"):
        sample_trans = transform(creditscore,geography,gender,age,tenure,balance,numofproducts,hascrcard,isactivemember,estimatedsalary)
        result=predict(sample_trans)
        if result[0] == 0:
            st.success('This customer is less likely to cancel the subscription !')
        else:
            st.warning('Warning ! This customer is more likely to cancel the subscription !')
            
if __name__=='__main__':
    main()
    
