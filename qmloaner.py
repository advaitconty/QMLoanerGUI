from pymongo import MongoClient
import pandas as pd
import secret
import certifi
import pdfs

# Function to load data from MongoDB
def load_data(item, client):
    db = client["inventory"]
    data = db[item]
    items = list(data.find())
    return items

# Function to confirm a loan
def confirm_loan(selected_number, client, option, confirm, name, clas):
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
        return "Failed. Guitar is not available for loan."

    # Define the update operation
    update_operation = {"$set": {"available": False}}

    # Perform the update operation
    result = collection.update_one({"_id": document_id}, update_operation)

    if result.modified_count > 0:
        pdf_path = load_loan_form(name=name, clas=clas, model=document["Brand"], id=document["_id"])
        return "Success! Loan form can be downloaded at {}".format(pdf_path)
    else:
        return "Failed to update the database"

def load_loan_form(name, clas, model, id):
    pdf_path = pdfs.create_loan_pdf(model, name, clas, id)
    return pdf_path
