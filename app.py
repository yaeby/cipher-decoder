import streamlit as st

pages = {
    "Home": [
        st.Page("pages\home.py", title="Homr"),
    ],
    "Decoders": [
        st.Page("pages\\frequency_analysis.py", title="Frequency Analysis"),
        st.Page("pages\delete.py", title="Playfair"),
    ],
}

pg = st.navigation(pages)
pg.run()