from pymongo import MongoClient
import streamlit as st
import pandas as pd
import secret
import certifi

def load_data(item):
    client = MongoClient(secret.mongo_host_connection("soote", "big", default=True), tlsCAFile=certifi.where())
    db = client["inventory"]
    data = db[item]
    counter = 1
    items = list(data.find())
    return pd.DataFrame(items)



def main():
    st.title("QuarterMaster Loaner System")

main()
option = st.selectbox(
        "What brand of guitar would you like to loan?",
        ("Alhambra", "Valencia", "Synchronium", "Y. Chai", "Other"),
    )

st.dataframe(load_data(option))

st.number_input("Enter the number of guitar you would like to ")