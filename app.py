import streamlit as st
import snowflake.connector
import pandas as pd
import time
import os

# Load env variables
user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")
account = os.getenv("SNOWFLAKE_ACCOUNT")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse="COMPUTE_WH",
    database="IOT_DB",
    schema="PUBLIC"
)

st.title("IoT Data Dashboard")

def load_data(query):
    return pd.read_sql(query, conn)

# AQI Trend
aqi_df = load_data("SELECT * FROM gold_aqi_trend")
st.subheader("AQI Trend")
st.line_chart(aqi_df.set_index("DATE"))

# Top Devices
top_df = load_data("SELECT * FROM gold_top_devices")
st.subheader("Top Devices")
st.bar_chart(top_df.set_index("DEVICE_ID"))

# Auto Refresh every 30 sec
time.sleep(30)
st.rerun()