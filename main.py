import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import toml
from datetime import datetime
import json
from utils import page_config

page_config()

try:
    google_sheets_creds = st.secrets["google_sheets"]

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

# ---------------------------------------

categories = {
    "Food"    : ["Lunch","Breakfast","Milk","Egg","Other"],
    "Grocery" : ["Dmart","Shopping","Other"],
    "Medicine": ["Insulin","Tablet","Other"],
    "Travel"  : ["Pass","Ticket","Other"],
    "Other"   : ["Rent","Other"],
}


st.title('Daily Expenses')
category  = st.selectbox("Category", options=["Food", "Grocery","Medicine","Travel", "Other"])

exp_form  = st.form("expense_entry")
item_name = exp_form.selectbox("Item", options= categories[category])
cost      = exp_form.number_input("Cost", min_value=0.0, value=20.00, step=10.00, format="%.2f")
date      = exp_form.date_input("Date", value=datetime.now())
description = exp_form.text_area("Description")
submitted = exp_form.form_submit_button("Submit")
    
if submitted:
    try:
        data = [category, item_name, cost, date.strftime("%Y-%m-%d"), description]
        sheet1.append_row(data)
    except Exception as e:
        print(e)    
    

## show google sheet data 
data = sheet1.get_all_records()
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)


