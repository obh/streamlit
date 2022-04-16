import streamlit as st
from datetime import datetime

def sayHello():
    st.write("hello world!")


def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.")
    st.button('Say hello', on_click=sayHello)

    #initial setup
    if 'count' not in st.session_state:
        st.session_state.count = 0

    merchantId = st.number_input('Enter MID')
    startTime = st.time_input("Start Time?", datetime.date(2022, 3, 1))
    endTime = st.time_input("End Time?", datetime.date(2022, 3, 31))
    submit = st.button('Submit')

    if submit:
        st.session_state.count += 1
        st.write("running for merchantID: ", merchantId)
        st.write("running from: ", startTime, " to ", endTime)


app()