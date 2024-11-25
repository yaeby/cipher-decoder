import streamlit as st

pages = {
    "Home": [
        st.Page("page\\home.py", title="Home"),
    ],
    "Ciphers": [
        st.Page("page\\frequency_analysis.py", title="Frequency Analysis"),
        st.Page("page\\playfair.py", title="Playfair Cipher"),
        st.Page("page\\des.py", title="DES Cipher"),
    ],
}

pg = st.navigation(pages)
pg.run()