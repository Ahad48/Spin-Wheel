import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

cats = pd.DataFrame([], columns=["Current Categories"])

if 'cat_df' not in st.session_state:
    st.session_state.cat_df = pd.DataFrame({
        "Current Categories": []
    })

if 'wheel' not in st.session_state:
    
    df = px.data.tips()
    st.session_state.wheel = px.pie(df, values='tip', names='day')

df = px.data.tips()
fig = px.pie(df, values='tip', names='day')


def add_new_row():
    
    new_row_data = {
        "Current Categories":st.session_state.new_cat
    }

    # Use pd.concat for the modern way to append rows
    st.session_state.cat_df = pd.concat([st.session_state.cat_df, pd.DataFrame([new_row_data])], ignore_index=True)
    
    st.session_state.new_cat = ""


def clear_state():
    for key in st.session_state.keys():
        del st.session_state[key]



with st.sidebar.form(key='new_row_form', clear_on_submit=True):
    new_cat = st.text_input("New Category", key="new_cat")
    submit_button = st.form_submit_button(label='Add Category', on_click=add_new_row)

if st.sidebar.button("Reset"):
    clear_state()


st.sidebar.dataframe(st.session_state.cat_df, width='stretch', hide_index=True)




tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", width='stretch')
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, width='stretch')