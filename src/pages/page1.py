import collections
from numpy.core.defchararray import lower
import streamlit as st


def sayHello():
    st.write("hello world!")


def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.")
    st.button('Say hello', on_click=sayHello)
