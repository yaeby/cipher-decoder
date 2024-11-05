import streamlit as st
from utils.PlayfairCipher import PlayfairCipher

st.title("Playfair Cipher")

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
        encrypeted = pf.playfair_encrypt(message)

    if(encrypeted != ""):
        st.write("Encrypted message: ", encrypeted)

with tab2:
    decrypted = ""
    message = st.text_area(label="Text to decrypt", placeholder="Enter the message to decrypt", height=200)

    if st.button("Decrypt"):
        decrypted = pf.playfair_decrypt(message)

    if(decrypted != ""):
        st.write("Decrypted message: ", decrypted)

