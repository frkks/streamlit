import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import datetime

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Prediction Car Price</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

filename = 'final_model_hearing'
model = pickle.load(open(filename, 'rb'))
hp_kW = st.sidebar.number_input("Hp KW:",min_value=5, max_value=300)
age = st.sidebar.number_input("Age:",min_value=0, max_value=15)
km = st.sidebar.number_input("KM:",min_value=0, max_value=500000)
Previous_Owners = st.sidebar.number_input("Previous Owners",min_value=0, max_value=4)
my_dict = {
    "hp_kW": hp_kW,
    "age": age,
    "km": km,
    "Previous_Owners": Previous_Owners,
}

df=pd.DataFrame.from_dict([my_dict])
st.table(df)
if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred)
    st.balloons()
    
    
img = Image.open("bmv.jpg")
st.image(img, caption="BMV", width=800)