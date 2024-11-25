import streamlit as st
from utils.DESCipher import DESCipher

st.title("DES (Data Encryption Standard)")

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
        height=100
    )

    if st.button("Encrypt", key="encrypt_button"):
        if len(key) != 8:
            st.error("Key must be exactly 8 characters long")
        else:
            try:
                # Create DES Cipher instance
                des_cipher = DESCipher(key)
                
                # Perform encryption
                encryption_details = des_cipher.encrypt(plaintext)
                
                # Display encryption results
                st.success(f"Encrypted Text: {encryption_details['final_cipher_text']}")
                
                # Display round details
                st.subheader("Encryption Rounds")
                for round_info in encryption_details['rounds']:
                    with st.expander(f"Round {round_info['round']}"):
                        st.write(f"Left Half (LPT): {round_info['lpt']}")
                        st.write(f"Right Half (RPT): {round_info['rpt']}")
                        st.write(f"Round Key: {round_info['round_key']}")
                        st.write(f"Expanded Result: {round_info['expanded_result']}")
                        st.write(f"XOR Result: {round_info['xor_result']}")
                        st.write(f"S-Box Substituted: {round_info['s_box_substituted']}")
                        st.write(f"P-Box Result: {round_info['p_box_result']}")
                
                # Display final binary and text
                st.subheader("Final Cipher")
                st.write(f"Binary: {encryption_details['final_cipher_binary']}")
                st.write(f"Text: {encryption_details['final_cipher_text']}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with tab2:
    ciphertext_input = st.text_area(
        label="Text to decrypt",
        placeholder="Enter the text to decrypt",
        height=100
    )

    if st.button("Decrypt", key="decrypt_button"):
        if len(key) != 8:
            st.error("Key must be exactly 8 characters long")
        else:
            try:
                # Create DES Cipher instance
                des_cipher = DESCipher(key)
                
                # Perform decryption
                decryption_details = des_cipher.decrypt(ciphertext_input)
                
                # Display decryption results
                st.success(f"Decrypted Text: {decryption_details['final_plaintext']}")
                
                # Display round details
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
                
                # Display final binary and text
                st.subheader("Final Plaintext")
                st.write(f"Binary: {decryption_details['final_plaintext_binary']}")
                st.write(f"Text: {decryption_details['final_plaintext']}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")