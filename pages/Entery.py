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

st.header('Daily Expense Enterys')
save_btn = st.button('save')

## show google sheet data 
sheet_data = sheet1.get_all_records()
for rec in sheet_data:
   date_str = rec.get('Date')
   rec['Date'] = datetime.strptime(date_str, '%Y-%m-%d').date()

sort_by_date = sorted(sheet_data, key=lambda item: item['Date'], reverse=True)


df = pd.DataFrame(sort_by_date)
df.index = np.arange(1, len(df)+1)
edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")
sorted_df = edited_df.sort_values(by='Date', ascending=False)
sorted_df['Date'] = sorted_df['Date'].astype(str)
df_to_records =[['Category', "Item Name", "Cost","Date", "Description"]] + sorted_df.values.tolist()

if save_btn:
    # print(df_to_records)
    sheet1.clear()
    sheet1.append_rows(df_to_records)

