import streamlit as st
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def page_config():
    st.set_page_config(layout='wide')

    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def get_spreadsheet():
    google_sheets_creds = st.secrets["google_sheets"]

    # Setup credentials for gspread
    creds = ServiceAccountCredentials.from_json_keyfile_dict(google_sheets_creds, [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ])
    
    client = gspread.authorize(creds)

    # Open the Google Sheets document by name
    spreadsheet = client.open("expense-manager")
    return spreadsheet
