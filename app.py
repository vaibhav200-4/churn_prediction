import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle

# load the model
model=tf.keras.models.load_model('model.h5')

# load the scaler and encoder
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)
with open('one_hot_encoder.pkl', 'rb') as f:
    one_hot_encoder = pickle.load(f)


st.title('Customer Churn Prediction')


geography = st.selectbox('Geography', one_hot_encoder.categories_[0].tolist())
gender=st.selectbox('Gender', label_encoder.classes_.tolist())
age=st.slider('Age', 18, 100)
balance=st.number_input('Balance', min_value=0.0,  step=100.0)
credit_score=st.slider('Credit Score') 
estimated_salary=st.number_input('Estimated Salary', min_value=0.0, step=100.0)
tenure=st.slider('Tenure', 0, 10)
num_of_products=st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

input_data = {
    
    'CreditScore':[credit_score],
    'Gender':[label_encoder.transform([gender])[0]], 
    'Age':[age],
    'Tenure':[tenure], 
    'Balance':[balance], 
    'NumOfProducts':[num_of_products], 
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member], 
    'EstimatedSalary':[estimated_salary], 
}
geo_encode=one_hot_encoder.transform([[geography]]).toarray()
geo_enco_df= pd.DataFrame(geo_encode, columns=['France', 'Germany', 'Spain'])

input_data = pd.concat([pd.DataFrame(input_data).reset_index(drop=True), geo_enco_df], axis=1)

input_data_scaled = scaler.transform(input_data)

prediction =model.predict(input_data_scaled)
prediction_prob=prediction[0][0]

st.write(f'Churn Probability: {prediction_prob:.2f}')

if prediction_prob > 0.5:
    st.write('Customer is likely to churn ')
else:
    st.write('Customer is likely to not churn')