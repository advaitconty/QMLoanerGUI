from pymongo import MongoClient
import streamlit as st
import pandas as pd
import secret
import certifi

# Function to load data from MongoDB
def load_data(item, client):
    db = client["inventory"]
    data = db[item]
    items = list(data.find())
    return items

# Function to confirm a loan
def confirm_loan(selected_number, client, option, confirm):
    if confirm:
        db = client["inventory"]
        collection = db[option]

        # Retrieve all documents from the collection
        documents = list(collection.find())

        # Check if selected_number is within range
        if selected_number < 0 or selected_number >= len(documents):
            st.error("Selected number is out of range")
            return

        # Select the document based on the index
        document = documents[selected_number]
        document_id = document['_id']

        # Check if the guitar is available
        if not document.get('available', True):
            st.session_state.error_message = "Guitar is not available for loan."
            return

        # Define the update operation
        update_operation = {"$set": {"available": False}}

        # Perform the update operation
        result = collection.update_one({"_id": document_id}, update_operation)

        # Print the number of documents updated
        if result.modified_count > 0:
            st.session_state.confirmation_message = "Loan confirmed. The DataFrame will refresh."
            st.session_state.refresh = True
        else:
            st.error("Failed to update the document")

# Function to handle the option change
def on_option_change():
    st.session_state.refresh = True

# Function to display the loan guitar form
def loan_guitar_form(client):
    st.title("QuarterMaster Loaner System")

    # Initialize session state variables
    if 'refresh' not in st.session_state:
        st.session_state.refresh = False

    if 'option' not in st.session_state:
        st.session_state.option = "Alhambra"

    if 'confirmation_message' not in st.session_state:
        st.session_state.confirmation_message = ""

    if 'error_message' not in st.session_state:
        st.session_state.error_message = ""

    # Option picker with callback
    option = st.selectbox(
        "What brand of guitar would you like to loan?",
        ("Alhambra", "Valencia", "Synchronium", "Y. Chai", "Other"),
        key='option',
        on_change=on_option_change
    )

    # Check if the data should be refreshed
    if st.session_state.refresh or 'data' not in st.session_state:
        data = load_data(option, client)
        st.session_state.data = pd.DataFrame(data)
        st.session_state.refresh = False

    # Display the DataFrame
    if 'data' in st.session_state:
        st.dataframe(st.session_state.data)

    with st.form(key='loan_guitar_form'):
        selected_number = st.number_input(
            "Enter the number of guitar you would like to loan (based on first column):",
            min_value=0,
            max_value=len(st.session_state.data) - 1,
            value=0
        )
        option2 = st.selectbox("Confirm?", (False, True))
        submitted = st.form_submit_button(
            label="Loan Guitar",
            help="Submit loan request",
        )

        if submitted:
            confirm_loan(selected_number, client, option, option2)
            st.experimental_rerun()

    # Display the confirmation message if available
    if st.session_state.confirmation_message:
        placeholder = st.empty()
        with placeholder.container():
            st.success(st.session_state.confirmation_message)
            if st.button("Close"):
                st.session_state.confirmation_message = ""
                placeholder.empty()
                st.experimental_rerun()

    # Display the error message if available
    if st.session_state.error_message:
        placeholder = st.empty()
        with placeholder.container():
            st.error(st.session_state.error_message)
            if st.button("Close"):
                st.session_state.error_message = ""
                placeholder.empty()
                st.experimental_rerun()

# Main function
def main():
    client = MongoClient(secret.mongo_host_connection("soote", "big", default=True), tlsCAFile=certifi.where())
    loan_guitar_form(client)

if __name__ == '__main__':
    main()
