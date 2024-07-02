import streamlit as st
import requests
import pandas as pd
import json
from io import StringIO

st.markdown(
    """ # Analysing HR data to predict and improve employee attrition rates.
    What is the probability that your current employee will leave the company, and what are the main factors due to influence this decision ?

    """
)
# ************************** Connection to API ***************************************
uploaded_file = st.file_uploader("Upload a json file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    json_data = json.loads(bytes_data)
    X = pd.DataFrame(json_data)
    st.write(f"## Description of employees")
    st.write(X)

    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app//upload_predict_leaving"

    # defining a params dict for the parameters to be sent to the API
    data = bytes_data

    # sending get request and saving the response as response object
    r = requests.post(url = URL, files = {'upload_file': data})

    st.write(f"## Ranking of employees based of probability of leaving the company:")
    ranking = json.loads(r.text)
    ranking_df = pd.DataFrame(ranking['Ranking'])
    st.write(ranking_df)
    # **************************************************************************************

else:
    st.write("Waiting for input...")
