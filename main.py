import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# Define the scope and credentials
scope = [
        "https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/drive"
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name(".streamlit/expense-manager-with-streamlit-2c0b9348d0b9.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("expance-manager").sheet1  # or specify the sheet name

# Access the Google Sheet
# sheet = client.open("sheet1").worksheet("expance-manager")

data = sheet.get_all_records() 
# print(data)

df = pd.DataFrame(data)

st.write(df)