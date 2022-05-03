import streamlit as st
from datetime import datetime
from datetime import date
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot():
    d = {'2022-02-01': [25.0, 75], '2022-02-02': [91, 92], '2022-02-03': [56, 67]}
    df = pd.DataFrame(d)
    df.index = ['pg1', 'pg2']
    #we will take inverse success rate
    df = 100 - df
    
    fig, ax = plt.subplots()
    palette = sns.color_palette("Blues", as_cmap=True)
    sns.heatmap(df, ax=ax, annot=df, cmap=palette)
    st.write("Failure rate for Refunds")
    st.write(fig)

def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.")

    #initial setup
    if 'count' not in st.session_state:
        st.session_state.count = 0

    merchantId = st.number_input('Enter MID')
    startTime = st.date_input("Start Time?", date.today())
    endTime = st.date_input("End Time?", date.today())
    submit = st.button('Submit')

    if submit:
        st.session_state.count += 1
        st.write("running for merchantID: ", merchantId)
        st.write("running from: ", startTime, " to ", endTime)

    plot()


app()
