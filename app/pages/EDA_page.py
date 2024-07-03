import streamlit as st
import requests
from io import StringIO

st.write('# This is EDA page')

import streamlit as st

plot = st.radio(
    "Choose your graph",
    ["Feature importance", "Time spent in the company",
     "Salary", "Number of projects", "Step counts"],
    captions = ["Short explanation", "Short explanation",
                "Short explanation", "Short explanation",
                "Short explanation"])

if plot == "Feature importance":
    # ************************** Connection to API : Feature importance ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_feature_importance"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************

if plot == "Time spent in the company":
        # ************************** Connection to API : Time spent in the company ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_time_spend_company"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************

if plot == "Salary":
    # ************************** Connection to API  : Salary ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_salary"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************


if plot == "Number of projects":
    # ************************** Connection to API :  Number of projects ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_number_projects"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************


if plot == "Step counts":
    # ************************** Connection to API ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_step_count"

    # sending get request and saving the response as response object
    # r = requests.post(url = URL, params = {'feature' : col})
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************
