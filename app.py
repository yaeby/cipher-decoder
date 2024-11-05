import streamlit as st

pages = {
    "Home": [
        st.Page("page\\home.py", title="Home"),
    ],
    "Ciphers": [
        st.Page("page\\frequency_analysis.py", title="Frequency Analysis"),
        st.Page("page\\playfair.py", title="Playfair Chiper"),
    ],
}

pg = st.navigation(pages)
pg.run()