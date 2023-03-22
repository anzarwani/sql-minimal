import streamlit as st
import pandas as pd
import sqlite3


uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, col1 TEXT, col2 TEXT)')
conn.commit()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file.name)
    df.to_sql('my_table', conn, if_exists='replace', index=False)

query = st.text_input('Enter your SQL query:')
if query:
    results = pd.read_sql_query(query, conn)
    st.write(results)
