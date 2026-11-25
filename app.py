import streamlit as st
import requests

# Sidebar
pages = {
    "Data Science": [
        st.Page("pages/predict.py", title="Zoologist Prediction"),
    ],
    "About": [
        st.Page("pages/about.py", title="About me"),
    ],
}

pg = st.navigation(pages)
pg.run()


# ## Header
# st.markdown("## 🐧 Zoologist")
