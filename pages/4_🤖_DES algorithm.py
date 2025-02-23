import streamlit as st
from utils.DESCipher import DESCipher

st.title("DES (Data Encryption Standard)")
st.sidebar.title("Block cipher :unlock:")
st.sidebar.caption("DES algorithm implementation")

with st.sidebar.expander("How it works", expanded=True):
    st.markdown("""
    - **Step 1:** Introduce a 8 charachter long key `(64bit)`.
    - **Step 2:** Then introduce a message that is also 8 characters long `(64bit)`.
    - **Step 3:** Now, you are free to encrypt or decrypt any message.
    - You can see the details of each rounds encryption or decryption process.
    """)

st.sidebar.info("""
Note: The implementation encrypts/decrypts only a block of 64 bits, it does not support multiple blocks.
"""
)

# Input section
key = st.text_input(
    label="Key (8 characters)", 
    placeholder="Enter an 8-character key",
    max_chars=8
)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
    plaintext = st.text_area(
        label="Text to encrypt",
        placeholder="Enter the message to encrypt",
        max_chars=8
        # height=100
    )

    if st.button("Encrypt", key="encrypt_button"):
        if len(key) != 8:
            st.error("Key must be exactly 8 characters long")
        else:
            try:
                des_cipher = DESCipher(key)
                
                encryption_details = des_cipher.encrypt(plaintext)
                
                st.success(f"Encrypted Text: {encryption_details['final_cipher_text']}")
                
                st.subheader("Encryption Rounds")
                for round_info in encryption_details['rounds']:
                    with st.expander(f"Round {round_info['round']}"):
                        st.write(f"Left Half (LPT): {round_info['lpt']}")
                        st.write(f"Right Half (RPT): {round_info['rpt']}")
                        st.write(f"Round Key: {round_info['round_key']}")
                        st.write("Function F:")
                        st.write(f"Expanded Result: {round_info['expanded_result']}")
                        st.write(f"XOR Result: {round_info['xor_result']}")
                        st.write(f"S-Box Substituted: {round_info['s_box_substituted']}")
                        st.write(f"P-Box Result: {round_info['p_box_result']}")
                
                st.subheader("Final Cipher")
                st.write(f"Binary: {encryption_details['final_cipher_binary']}")
                st.write(f"Text: {encryption_details['final_cipher_text']}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with tab2:
    ciphertext_input = st.text_area(
        label="Text to decrypt",
        placeholder="Enter the text to decrypt",
        max_chars=8
        # height=100
    )

    if st.button("Decrypt", key="decrypt_button"):
        if len(key) != 8:
            st.error("Key must be exactly 8 characters long")
        else:
            try:
                des_cipher = DESCipher(key)
                
                decryption_details = des_cipher.decrypt(ciphertext_input)
                
                st.success(f"Decrypted Text: {decryption_details['final_plaintext']}")
                
                st.subheader("Decryption Rounds")
                for round_info in decryption_details['rounds']:
                    with st.expander(f"Round {round_info['round']}"):
                        st.write(f"Left Half (LPT): {round_info['lpt']}")
                        st.write(f"Right Half (RPT): {round_info['rpt']}")
                        st.write(f"Round Key: {round_info['round_key']}")
                        st.write(f"Expanded Result: {round_info['expanded_result']}")
                        st.write(f"XOR Result: {round_info['xor_result']}")
                        st.write(f"S-Box Substituted: {round_info['s_box_substituted']}")
                        st.write(f"P-Box Result: {round_info['p_box_result']}")
                
                st.subheader("Final Plaintext")
                st.write(f"Binary: {decryption_details['final_plaintext_binary']}")
                st.write(f"Text: {decryption_details['final_plaintext']}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")