import streamlit as st
from utils.VigenereCipher import VigenereCipher

st.title("Vigenère Cipher")
st.sidebar.title("Vigenère Cipher :memo:")
st.sidebar.caption("Vigenère implementation")
with st.sidebar.expander("How it works", expanded=True):
    st.markdown("""
    - **Step 1:** Introduce a key.
    - **Step 2:** Select a tab `Encrypt` or `Decrypt`.
    - **Step 3:** Introduce a message to encrypt or decrypt.
    - Verify using `Tabula Recta` (the classical Vigenère cipher tableau).
    """)

st.sidebar.info("""
Only English language is supported.
"""
)

key = st.text_input(label="Key", placeholder="Enter the key")
vc = VigenereCipher(key=key)
tab1, tab2, tab3 = st.tabs(["Encrypt", "Decrypt", "Tabula Recta"])

with tab1:
    encrypeted = ""
    message = st.text_area(label="Text to encrypt", placeholder="Enter the message to encrypt", height=200)
    if st.button("Encrypt"):
        encrypeted = vc.encrypt(message)
    if encrypeted:
        st.write("Encrypted message: ", encrypeted)

with tab2:
    decrypted = ""
    message = st.text_area(label="Text to decrypt", placeholder="Enter the message to decrypt", height=200)
    if st.button("Decrypt"):
        decrypted = vc.decrypt(message)
    if decrypted:
        st.write("Decrypted message: ", decrypted)

with tab3:
    st.write("### Tabula Recta")
    tabula_recta = vc.generate_tabula_recta()
    st.dataframe(tabula_recta)