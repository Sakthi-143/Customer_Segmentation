#!/usr/bin/env python
# coding: utf-8

# # Moodel Deployment

# In[ ]:


# Load libraries
import pandas as pd
import streamlit as st
from sklearn.svm import SVC
from pickle import load

# Title of the web app
st.title('Customer Personality Analysis')

# Sidebar for user input
st.sidebar.header('User Input Parameters')

# Function to take user input
def user_input_features():
    Education = st.sidebar.selectbox('Select your education level', ['Basic','Graduation','Masters','phD','2n Cycle'], index=0)
    Marital_Status = st.sidebar.selectbox('Select Marital Status', ['Single', 'Married', 'Together', 'Divorced', 'Widow', 'Alone'], index=0)
    Income = st.sidebar.number_input('Income per Annual')
    Kidhome = st.sidebar.number_input("Kids in Home")
    Teenhome = st.sidebar.number_input("Teen in Home")
    Recency = st.sidebar.number_input("Recency")
    MntWines = st.sidebar.number_input("MntWines")
    MntFruits = st.sidebar.number_input("MntFruits")
    MntMeatProducts = st.sidebar.number_input("MntMeatProducts")
    MntFishProducts = st.sidebar.number_input("MntFishProducts")
    MntSweetProducts = st.sidebar.number_input("MntSweetProducts")
    MntGoldProds = st.sidebar.number_input("MntGoldProds")
    data = {'Education':Education,
            'Marital_Status':Marital_Status,
            'Income':Income,
            'Kidhome':Kidhome,
            'Teenhome':Teenhome,
            'Recency': Recency,
            'MntWines' : MntWines,
            'MntFruits' : MntFruits,
            'MntMeatProducts' : MntMeatProducts,
            'MntFishProducts' : MntFishProducts,
            'MntSweetProducts' : MntSweetProducts,
            'MntGoldProds': MntGoldProds}
    features = pd.DataFrame(data, index=[0])
    return features 

# Display user inputs
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# Load the trained model
loaded_model = load(open("final_model.pkl", 'rb'))

# Preprocess input data (one-hot encoding)
df = pd.get_dummies(df, columns=['Education', 'Marital_Status'])

# Make predictions and display the result
prediction = loaded_model.predict(df)

st.subheader('Predicted Result')


def segment_customers(input_data):

    prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Kidhome','Teenhome','Age','Partner','Education_Level']))
    print(prediction)
pred_1 = ''

if prediction[0] == 0:
    pred_1 = 'cluster 0'
elif prediction[0] == 1:
    pred_1 = 'cluster 1'
elif prediction[0] == 2:
    pred_1 = 'cluster 2'
elif prediction[0] == 3:
    pred_1 = 'cluster 3'

st.write(f'The predicted cluster is: {pred_1}')


