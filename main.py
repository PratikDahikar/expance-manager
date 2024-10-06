import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from datetime import datetime
from utils import page_config, get_spreadsheet

try:
    page_config()
    spreadsheet = get_spreadsheet()

    # Access specific worksheets by their names
    sheet1 = spreadsheet.worksheet("sheet1")  
    sheet2 = spreadsheet.worksheet("sheet2") 
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
df.index = np.arange(1, len(df)+1)
st.dataframe(df, use_container_width=True)


