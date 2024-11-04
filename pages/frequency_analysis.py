import streamlit as st
import pandas as pd
from utils.TextAnalyzer import TextAnalyzer

letter_freqs = {
    'Letter': ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'],
    'Frequency': [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0, 2.0, 1.9, 1.5, 1.0, 0.8, 0.15, 0.15, 0.10, 0.07]
}

# st.set_page_config(
#     layout="centered",
#     page_title="Frequency Analysis"
#     )

st.sidebar.title("Mono-alphabetic cipher decoder:unlock:")
st.sidebar.caption("A mono-alphabetic ciphertext decoder that analyzes the frequency of characters.")
st.sidebar.caption("Made by [who ego znaet](https://www.linkedin.com/in/adrian-copta-9058bb291/) :alien:")

with st.sidebar.expander("How it works", expanded=True):
    st.markdown("""
    - **Step 1:** Introduce the intercept (the encrypted text) in the provided text area and `Start Frequency Analysis`.
    - **Step 2:** The app will analyze the encryption and provide insights into the letter frequencies and patterns.
    - **Step 3:** You can then map letters to other ecrypted letters to modify the ciphertext and `Apply` changes in real-time.
    - When all the letters are mapped and the text is decrypted, you will see some magic. :balloon:
    """)

st.sidebar.info("""
Note: This decoder only helps you decipher encrypted text and is intended solely for the English language.
"""
)


st.title("Frequency Analysis")

if 'ANALYZER' not in st.session_state:
    st.session_state['ANALYZER'] = None

intercept = st.text_area(label="Intercept", placeholder="Enter the intercept", height=300)


if st.button('Start Frequency Analysis'):
    st.session_state['ANALYZER'] = TextAnalyzer(intercept)

ANALYZER = st.session_state['ANALYZER']

st.divider()

if ANALYZER:

    col1, col2, col3 = st.columns([1.5, 3.5, 0.6])

    letter_freqs_df = pd.DataFrame(letter_freqs)
    col1.data_editor(
        letter_freqs_df,
        # column_config={
        #     "Frequency": st.column_config.ProgressColumn(
        #         label="Frequency",
        #         min_value=0,
        #         max_value=15,
        #         format="%f"
        #     )
        # }, 
        disabled=True, 
        hide_index=True
        )

    df = ANALYZER.get_letter_frequencies()
    max_value = int(df['Count'].max())

    edited_df = col2.data_editor(
        df,
        column_config={
        "Count": st.column_config.ProgressColumn(
            label="Count",
            min_value=0,
            max_value=max_value,
            format="%d"
        ),
        "Matching_letter": st.column_config.SelectboxColumn(
            label="Replace",
            options=[
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z'
            ]
        )
        }, 
        disabled=False,
        hide_index=True
    )

    if col3.button("Apply"):
        replaced_text = ANALYZER.replace_letters(edited_df)
        st.text_area(label='Ciphertext', value=replaced_text, height=300, disabled=True)
        
        if not (edited_df['Matching_letter'].isnull().any() or (edited_df['Matching_letter'] == '').any()):
            print("All matching letters are completed.")
            print("Decoded text: \n" + replaced_text)
            st.balloons()
    else:
        st.text_area(label='Ciphertext', value=intercept, height=300, disabled=True)

    st.divider()

    with st.expander("Digraphs", expanded=True):
        eng_dig = ['TH','HE','AN','IN','ER','ON','RE','ED','ND','HA','AT','EN']
        st.write("The most common **digraphs** in the english language are:")
        st.dataframe(pd.DataFrame(eng_dig).T)

        st.write("The most common **digraphs** in the message are:")
        digraph_counts = ANALYZER.count_digraphs()
        df = pd.DataFrame.from_dict(digraph_counts, orient='index', columns=['Count'])
        st.dataframe(df.T)
        

    with st.expander("Trigraphs", expanded=True):
        eng_tri = ['THE', 'AND', 'THA', 'ENT', 'ION', 'TIO', 'FOR', 'NDE', 'HAS', 'NCE', 'TIS', 'OFT', 'MEN']
        st.write("The most common **trigraphs** in the English language are:")
        st.dataframe(pd.DataFrame(eng_tri).T)

        st.write("The most common **trigraphs** in the message are:")
        trigraphs_count = ANALYZER.count_trigraphs()
        df = pd.DataFrame.from_dict(trigraphs_count, orient='index', columns=['Count'])
        st.dataframe(df.T)


    with st.expander("Doubles", expanded=True):
        eng_doubles = ['SS', 'EE', 'TT', 'FF', 'LL', 'MM', 'OO']
        st.write("The most common **double letters** in the English language are:")
        st.dataframe(pd.DataFrame(eng_doubles).T)

        st.write("The most common **double letters** in the message are:")
        doubles_count = ANALYZER.count_doubles()
        df = pd.DataFrame.from_dict(doubles_count, orient='index', columns=['Count'])
        st.dataframe(df.T)
