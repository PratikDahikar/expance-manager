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
#-----------------------------------
## -------Graph-------

st.title('Monthly Analysis')
data = sheet1.get_all_records()
sheet_data = {}
for item in data:
    item_cat = item['Category'] 
    sheet_data[item_cat] = sheet_data.get(item_cat, 0) + item.get('Cost')

data = {
    "Category": sheet_data.keys(),
    "Cost": sheet_data.values()
}
# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
st.bar_chart(data=df, x='Category', y='Cost')
##-----------------------------------









