import streamlit as st

pages = {
    "Home": [
        st.Page("pages\home.py", title="Home"),
    ],
    "Ciphers": [
        st.Page("pages\\frequency_analysis.py", title="Frequency Analysis"),
        st.Page("pages\playfair.py", title="Playfair Chiper"),
    ],
}

pg = st.navigation(pages)
pg.run()