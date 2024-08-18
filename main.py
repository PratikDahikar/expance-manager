import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import toml
from datetime import datetime
import json

google_sheets_creds = st.secrets["google_sheets"]
try:
    # Setup credentials for gspread
    creds = ServiceAccountCredentials.from_json_keyfile_dict(google_sheets_creds, [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ])
    client = gspread.authorize(creds)

    # Open the Google Sheets document by name
    spreadsheet = client.open("expense-manager")

    # Access specific worksheets by their names
    sheet1 = spreadsheet.worksheet("sheet1")  # Replace "Sheet1" with your actual worksheet name
    sheet2 = spreadsheet.worksheet("sheet2")  # Replace "Sheet2" with your actual worksheet name
except Exception as e:
    print(e)

# Streamlit form
with st.form("expense_entry",clear_on_submit=True):
    st.header("Expense Entry")
    category = st.selectbox("Category", ["Food", "Grocery","Medicine","Travel", "Other"])
    item_name = st.text_input("Item")
    cost = st.number_input("Cost", min_value=0.0, value=20.00, step=10.00, format="%.2f")
    date = st.date_input("Date", value=datetime.now())
    description = st.text_area("Description")

    submitted = st.form_submit_button("Submit")
    
if submitted:
    try:
        data = [category, item_name, cost, date.strftime("%Y-%m-%d"), description]
        sheet1.append_row(data)
    except Exception as e:
        print(e)    
    
    
data = sheet1.get_all_records()
df = pd.DataFrame(data)
# st.write(df)
st.dataframe(df, use_container_width=True)

# data = sheet2.get_all_records()
# df = pd.DataFrame(data)
# st.write(df)