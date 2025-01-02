import streamlit as st
from utils.PlayfairCipher import PlayfairCipher

st.title("Playfair Cipher")

st.sidebar.title("Playfair cipher :unlock:")
st.sidebar.caption("Playfair implementation")
with st.sidebar.expander("How it works", expanded=True):
    st.markdown("""
    - **Step 1:** Introduce a key.
    - **Step 2:** Select a language.
    - **Step 3:** Introduce a message to encrypt or decrypt.
    - Verify using playfair tabel.
    """)

st.sidebar.info("""
Note: Only two languages are supported, English and Romanian.
"""
)

key = st.text_input(label="Key", placeholder="Enter the key")

choice = st.radio("Choose the alphabet", ["English", "Romanian"])

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

if choice == "Romanian":
    alphabet = 'AĂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

pf = PlayfairCipher(key=key, alphabet=alphabet)

tab1, tab2 =st.tabs(["Encrypt", "Decrypt"])

with tab1:
    encrypeted = ""
    message = st.text_area(label="Text to encrypt", placeholder="Enter the message to encrypt", height=200)

    if st.button("Encrypt"):
        encrypeted, square = pf.playfair_encrypt(message)

    if(encrypeted != ""):
        st.write("Encrypted message: ", encrypeted)
        st.table(square)

with tab2:
    decrypted = ""
    message = st.text_area(label="Text to decrypt", placeholder="Enter the message to decrypt", height=200)

    if st.button("Decrypt"):
        decrypted, square = pf.playfair_decrypt(message)

    if(decrypted != ""):
        st.write("Decrypted message: ", decrypted)
        st.table(square)

