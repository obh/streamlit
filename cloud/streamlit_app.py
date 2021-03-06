import streamlit as st
import plotly.express as px
import math
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def highlight_survived(val):
    failure_rate = int(val.split(" ")[0])
    g = 245 - (245 * failure_rate)/100
    b = 245 - (245 * failure_rate)/100
    col = "rgb(255, " + str(g) + "," + str(b) + ")"
    st.write(failure_rate)
    return f'background-color: {col}' 


def plot():
    d = {'2022-02-01': [0.0, 75.1283129318], '2022-02-02': [91, 92.1283129318], '2022-02-03': [56, 67.8123131231]}
    c = {'2022-02-01': [10, 175], '2022-02-02': [191, 2], '2022-02-03': [6, 6]}
    df = pd.DataFrame(d)
    countDf = pd.DataFrame(c)
    df.index = ['pg1', 'pg2']
    countDf.index = ['pg1', 'pg2']

    #we will take inverse success rate
    df = 100 - df
    cm = sns.light_palette("green", as_cmap=True)
    df.style.background_gradient(cmap=cm)

    df_str = df.applymap(lambda x: f'{x:.0f}' if not pd.isnull(x) else '')
    countDf_str = countDf.applymap(lambda x: f'{x:.0f}' if not pd.isnull(x) else '')
    annotDf = df_str + " (" + countDf_str + ")"
    st.dataframe(annotDf.style.applymap(highlight_survived))

    #st.write(df)
    #st.write(annotDf)
    #fig, ax = plt.subplots()
    #palette = sns.color_palette("Reds", as_cmap=True)
    #sns.heatmap(df, ax=ax, annot=annotDf, cmap=palette, fmt='')
    #st.subheader("Failure rate for Refunds")
    #st.write(fig)

def plot2():
    df = pd.read_csv("https://raw.githubusercontent.com/obh/streamlit/main/cloud/q2.csv")
    st.line_chart(df)
    #fig, ax = plt.subplots()
    #sns.lineplot(data=df, ax=ax, x="week", y="refundcount",  markers=True)
    #st.subheader("Refunds More than 7 days")
    #st.write(fig)

def plot3():
    df = pd.read_csv("https://raw.githubusercontent.com/obh/streamlit/main/cloud/q3.csv")
    df = df.pivot("date", columns=["age"], values="total")
    df = df.fillna(0)
    less_than_4days = df[ [x for x in df.columns.to_list() if x <= 96] ]
    more_than_1day = df[ [x for x in df.columns.to_list() if x > 24] ]

    p90 = more_than_1day.apply(lambda x: np.percentile(x, 90), axis=1)
    p95 = more_than_1day.apply(lambda x: np.percentile(x, 95), axis=1)
    p99 = more_than_1day.apply(lambda x: np.percentile(x, 99), axis=1)
    merged_df = pd.concat([p90, p95, p99], axis = 1)
    merged_df.columns = ["90th percentile", "95th percentile", "99th percentile"]
    rows = merged_df.index.to_list()

    st.dataframe(merged_df)
    fig, ax = plt.subplots()
    fig = px.line(merged_df, y = ['90th percentile', '95th percentile', '99th percentile'], 
            title='Refund Processing Time',
            labels={"value": "Hours to Process Refund", "variable": "Thresholds"})
    st.write(fig)

    #now lets print the second part
    total_refunds = df.sum(axis = 1)
    less_than_4days = less_than_4days.sum(axis = 1)
    percentile = less_than_4days / total_refunds
    percentile = pd.DataFrame(percentile)
    percentile.columns = ["% processed"]
    percentile = percentile.reset_index()
    st.dataframe(percentile)
    fig, ax = plt.subplots()
    fig = px.area(percentile, x='date', y='% processed', markers=True, title = 'API Refund Processing %')
    st.write(fig)


def line_chart_series(data, x_axis, y_axis):
        c = alt.Chart(data).mark_line().encode(x=x_axis, y=y_axis, tooltip=[x_axis, y_axis])
        st.altair_chart(c, use_container_width=True)
    

def xtick_visibility(ax, max_labels):
    xticks=ax.xaxis.get_major_ticks()
    stepper =  max(1, (len(xticks) -1) / max_labels)
    stepper = math.ceil(stepper) 
    st.write(stepper)
    
    for i in range(len(xticks)):
        if (i + 1) % stepper == 0 and stepper != 1:
            xticks[i].set_visible(False)


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
    
    st.write("hello world!")
    plot()
    plot2()
    plot3()


app()
