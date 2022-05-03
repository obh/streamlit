import streamlit as st
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot():
    d = {'2022-02-01': [0.0, 75.1283129318], '2022-02-02': [91, 92.1283129318], '2022-02-03': [56, 67.8123131231]}
    c = {'2022-02-01': [10, 175], '2022-02-02': [191, 2], '2022-02-03': [6, 6]}
    df = pd.DataFrame(d)
    countDf = pd.DataFrame(c)
    df.index = ['pg1', 'pg2']
    countDf.index = ['pg1', 'pg2']

    #we will take inverse success rate
    df = 100 - df
    df_str = df.applymap(lambda x: f'{x:.0f}' if not pd.isnull(x) else '')
    countDf_str = countDf.applymap(lambda x: f'{x:.0f}' if not pd.isnull(x) else '')
    annotDf = df_str + " (" + countDf_str + ")"
    st.write(df)
    st.write(annotDf)
    fig, ax = plt.subplots()
    palette = sns.color_palette("Reds", as_cmap=True)
    sns.heatmap(df, ax=ax, annot=annotDf, cmap=palette, fmt='')
    st.subheader("Failure rate for Refunds")
    st.write(fig)

def plot2():
    d = np.array([[17, 'cybyes', 2, 10], [17, 'cybyes', 1, 24], [17, 'yesupi', 10, 3]])
    df = pd.DataFrame(d)
    p = df.pivot(['mid', 'pg'], columns='refunddays')


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
