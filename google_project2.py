#DATA CLEANING & PREPARATION
import pandas as pd

df = pd.read_csv("C:/Users/HP/Downloads/Play Store Data.csv")

# Clean Installs
df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Clean Category
df['Category'] = df['Category'].astype(str)

# Drop null installs
df = df.dropna(subset=['Installs'])


#APPLY CATEGORY NAME FILTER

excluded_letters = ('A', 'C', 'G', 'S')

df = df[~df['Category'].str.startswith(excluded_letters)]
#AGGREGATE GLOBAL INSTALLS BY CATEGORY

category_installs = (
    df.groupby('Category')['Installs']
    .sum()
    .reset_index()
)
#FILTER CATEGORIES WITH INSTALLS > 1 MILLION

category_installs = category_installs[
    category_installs['Installs'] > 1_000_000
]
#SELECT TOP 5 CATEGORIES (CORE LOGIC)

top5_categories = (
    category_installs
    .sort_values(by='Installs', ascending=False)
    .head(5)
)
#CREATE CHOROPLETH MAP
import plotly.express as px

fig = px.choropleth(
    top5_categories,
    locations=["World"] * len(top5_categories),
    locationmode="ISO-3",
    color="Installs",
    hover_name="Category",
    color_continuous_scale="viridis",
    title="Global Installs by Top 5 App Categories"
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True),
    margin=dict(l=0, r=0, t=40, b=0)
)

#TIME-BASED VISIBILITY

from datetime import datetime
import pytz
import streamlit as st

ist = pytz.timezone('Asia/Kolkata')
current_hour = datetime.now(ist).hour

if 18 <= current_hour < 20:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("🌙 This visualization is available only between 6 PM and 8 PM IST.")









