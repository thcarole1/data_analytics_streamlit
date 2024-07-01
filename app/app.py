import streamlit as st
import requests
import pandas as pd
import json
from io import StringIO

# if 'page' not in st.session_state:
#         st.session_state.page = 'Home'

# # Define pages
# def home():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page")

#     if st.button('Go to Page 1'):
#                 st.session_state.page = 'Page 1'
#     if st.button('Go to Page 2'):
#                 st.session_state.page = 'Page 2'
#     if st.button('Go to Page 3'):
#                 st.session_state.page = 'Page 3'

# def page1():
#     st.title("Page 1")
#     st.write("Welcome to Page 1")
#     if st.button('Go to Home'):
#                 st.session_state.page = 'Home'

# def page2():
#     st.title("Page 2")
#     st.write("Welcome to Page 2")
#     if st.button('Go to Home'):
#                 st.session_state.page = 'Home'

# def page3():
#     st.title("Page 3")
#     st.write("Welcome to Page 3")
#     if st.button('Go to Home'):
#                 st.session_state.page = 'Home'

# # Display the selected page
# if st.session_state.page == 'Home':
#     home()
# elif st.session_state.page == 'Page 1':
#     page1()
# elif st.session_state.page == 'Page 2':
#     page2()
# elif st.session_state.page == 'Page 3':
#     page3()


# url = 'https://file-us-3.sendbird.com/4458ae52de1e4146b1a6c08e2939d7bd.png?auth=aHC8odu2s_CoY9f2dIQQ2u8Oofk9YAHKmOY-tq7AGuh8E52La3iUaYOJCFf3Fm8ml5lVfdDX1KhI8hR_9L6W7A'
# st.image(url)


st.markdown(
    """ # HR Data analytics
    ## Analysing HR data to predict and improve employee attrition rates.
    What is the probability that your current employee will leave the company, and what are the main factors due to influence this decision ?

    """
)


uploaded_file = st.file_uploader("Upload a json file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

json_data = json.loads(bytes_data)
X = pd.DataFrame(json_data)
st.write(f"## Description of candidates")
st.write(X)


# api-endpoint
URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/upload_predict_hiring"
st.write(f"Path to API is : {URL}")

# defining a params dict for the parameters to be sent to the API
data = bytes_data

# sending get request and saving the response as response object
r = requests.post(url = URL, files = {'upload_file': data})

st.write(f"## Ranking of applicants based of probability to stay with the company:")
content = json.loads(r.text)
st.write(content)
