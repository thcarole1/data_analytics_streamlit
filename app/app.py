import streamlit as st

st.set_page_config(page_title="HR Data analytics")
st.markdown(
    """ # HR Data analytics
    """
)

homepage = st.Page("pages/homepage.py", title="Homepage")
EDA_page = st.Page("pages/EDA_page.py", title="EDA")
hiring_page = st.Page("pages/hiring_page.py", title="Hiring")
leaving_page = st.Page("pages/leaving_page.py", title="Leaving")

pg = st.navigation([homepage, EDA_page, hiring_page, leaving_page])
pg.run()
