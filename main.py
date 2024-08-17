import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import toml

# Load the TOML file
# config = toml.load(st.secrets["google_sheets"])

print('loading google creds')
# Extract credentials from the TOML file
# google_sheets_creds = config['google_sheets']
google_sheets_creds = st.secrets["google_sheets"]

print('loading google creds complete')

# Setup credentials for gspread
creds = ServiceAccountCredentials.from_json_keyfile_dict(google_sheets_creds, [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
])

client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("expance-manager").sheet1  # or specify the sheet name

Access the Google Sheet
sheet = client.open("sheet1").worksheet("expance-manager")

data = sheet.get_all_records() 
print(data)

df = pd.DataFrame(data)

st.write(df)

st.write('welcome to streamlit ...!!!')