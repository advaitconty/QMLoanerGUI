from pymongo import MongoClient
import streamlit as st
import pandas as pd
import secret
import certifi

runs = 0
previous_set = ""

def load_data(item, client):
    db = client["inventory"]
    data = db[item]
    counter = 1
    items = list(data.find())
    return items

def loan_guitar(selected_number, guitar, client, option, confirm):
    if confirm:
        db = client["inventory"]
        guitars = db[option]
        document = list(guitars.find(guitar[selected_number]))
        update_operation = {"$set": {"available": False}}
        result = guitars.update_one(update_operation, document)
        print(result)

def loan_guitar_form(client):
    selected_number = 0
    st.title("QuarterMaster Loaner System")
    option = st.selectbox(
        "What brand of guitar would you like to loan?",
        ("Alhambra", "Valencia", "Synchronium", "Y. Chai", "Other"),
    )
    data = load_data(option, client)
    st.dataframe(pd.DataFrame(data))
    with st.form(key='loan_guitar_form'):
        st.number_input("Enter the number of guitar you would like to loan (based on first column):", min_value=0,
                    max_value=(len(data) - 1),
                    value=selected_number)
        option2 = st.selectbox(
            "Confirm?",
            (False, True),
        )
        st.form_submit_button(label="Loan Guitar", help="Submit loan request",
                          on_click=loan_guitar(selected_number, data, client, option, option2))

def main():
    client = MongoClient(secret.mongo_host_connection("soote", "big", default=True), tlsCAFile=certifi.where())
    loan_guitar_form(client)

if __name__ == '__main__':
    main()