import streamlit as st
import numpy as np
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# rows = st.sidebar.text_input('cats', "Category", placeholder='Enter Category')
# cols = st.columns(rows)

cats = pd.DataFrame([], columns=["Current Categories"])

if 'cat_df' not in st.session_state:
    st.session_state.cat_df = pd.DataFrame({
        "Current Categories": []
    })



def add_new_row():
    
    new_row_data = {
        "Current Categories":st.session_state.new_cat
    }

    # Use pd.concat for the modern way to append rows
    st.session_state.cat_df = pd.concat([st.session_state.cat_df, pd.DataFrame([new_row_data])], ignore_index=True)
    
    st.session_state.new_cat = ""




with st.sidebar.form(key='new_row_form', clear_on_submit=True):
    new_cat = st.text_input("New Category", key="new_cat")
    submit_button = st.form_submit_button(label='Add Category', on_click=add_new_row)

st.sidebar.dataframe(st.session_state.cat_df, width='stretch', hide_index=True)

